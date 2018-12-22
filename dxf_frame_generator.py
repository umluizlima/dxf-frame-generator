"""DXF Frame Generator.

This module generates DXF files for laser cutting custom sized frames, which
can be easily manufactured at the nearest FabLab.

Example
-------
Generate a frame that fits an A4 sized sheet:

    $ python -m dxf_frame_generator 210 297

This will create a 'frame_210x297.dxf' file on the current working directory.

"""
import os.path
import ezdxf


class Frame():
    """Frame generator class."""

    dwg = ezdxf.new('R2010')
    dwg.layers.new(name='CUT', dxfattribs={'color': 7})
    msp = dwg.modelspace()

    front = 25  # width of the front sides
    back = 15   # width of the back sides
    offset = 0  # distance between front and back patterns

    def __init__(self, width: int, height: int):
        """Initialize a new Frame instance."""
        if width > height:
            width, height = height, width

        self.width = width
        self.height = height

    def draw(self):
        """Draw the frame."""
        outer_width = 2 * self.back + self.width
        outer_height = 2 * self.back + self.height

        self._draw_back(outer_width, outer_height)
        self._draw_front(outer_width, outer_height)

        self._save()

    def _draw_back(self, outer_width, outer_height):
        """Draw the back pattern of a frame, starting on origin (0, 0)."""
        rectangles = [
            [
                (0, 0),
                (outer_width, 0),
                (outer_width, outer_height),
                (0, outer_height)
            ],
            [
                (self.back, self.back),
                (outer_width - self.back, self.back),
                (outer_width - self.back, outer_height - self.back),
                (self.back, outer_height - self.back)
            ]
        ]
        for rect in rectangles:
            self.msp.add_lwpolyline(
                rect, dxfattribs={'layer': 'CUT', 'closed': True})

        radius = self.back / 4
        circles = [
            (self.back / 2, self.back / 2),
            (self.back / 2, outer_height / 2),
            (self.back / 2, outer_height - self.back / 2),
            (outer_width / 2, outer_height - self.back / 2),
            (outer_width / 2, self.back / 2),
            (outer_width - self.back / 2, self.back / 2),
            (outer_width - self.back / 2, outer_height / 2),
            (outer_width - self.back / 2, outer_height - self.back / 2)
        ]
        for center in circles:
            self.msp.add_circle(center, radius, dxfattribs={'layer': 'CUT'})

    def _draw_front(self, outer_width, outer_height):
        """Draw the front pattern of a frame, starting from offset point."""
        offset = outer_width + self.offset
        rectangles = [
            [
                (offset, 0),
                (offset + outer_width, 0),
                (offset + outer_width, outer_height),
                (offset, outer_height)
            ],
            [
                (offset + self.front, self.front),
                (offset + outer_width - self.front, self.front),
                (offset + outer_width - self.front, outer_height - self.front),
                (offset + self.front, outer_height - self.front)
            ]
        ]
        for rect in rectangles:
            self.msp.add_lwpolyline(
                rect, dxfattribs={'layer': 'CUT', 'closed': True})

    def _save(self):
        """Save frame to filesystem."""
        filename = f'frame_{self.width}x{self.height}.dxf'
        self.dwg.saveas(filename)
        print(os.path.abspath(filename), end='')


def run():
    """Draw a frame from CLI arguments."""
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Generate frames for digital fabrication.")
    parser.add_argument(
        "width", metavar="W", type=int,
        help="an integer for the frame's inner width, in milimeters."
    )
    parser.add_argument(
        "height", metavar="H", type=int,
        help="an integer for the frame's inner height, in milimeters."
    )
    args = parser.parse_args()

    f = Frame(args.width, args.height)
    f.draw()


if __name__ == '__main__':
    run()
