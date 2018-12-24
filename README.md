# DXF Frame Generator
> Quickly create frames for digital fabrication.

Generate DXF files for laser cutting custom sized frames, which can then be easily manufactured at the nearest FabLab.

A frame is made by two sheets glued together, with regular wooden glue, and then painted with acrylic dye. It has holes on its back to be hung on the wall.

Here's a finished frame, after gluing and painting:

![Frame that has been manufactured from a dxf produced by this script.](https://user-images.githubusercontent.com/9170476/50379241-97b39580-062b-11e9-8f0b-10e60ca88d9b.jpg)

Customized illustration by [@moraesnika](https://instagram.com/moraesnika), at [N Design](https://instagram.com/lojandesign).

## Description

This project consists of a Python script that takes two Integers as arguments to draw a frame's 2D profile of the given size.

The output file has the **.dxf** extension, which can be used for laser cutting.

## Installation

- Windows

```sh
pip install dxf-frame-generator
```

- Linux

```sh
sudo pip3 install dxf-frame-generator
```

## Usage example

The following command will create a file `frame_200x200.dxf` on the current working directory:

```sh
> dxf-frame-generator 200 200
path\to\current\directory\frame_210x297.dxf
```

This is how the file looks like when imported on a laser fabrication software:
![DXF file when imported on a laser fabrication software.](https://user-images.githubusercontent.com/9170476/50379245-bc0f7200-062b-11e9-9054-573435e4fe03.png)

## Changelog

- 0.0.1: Initial release;

## Links
- Repository: https://github.com/umluizlima/dxf-frame-generator
- Issue tracker: https://github.com/umluizlima/dxf-frame-generator/issues
- References:
  - Mozman's **ezdxf** package: https://github.com/mozman/ezdxf
  - RDWorksV8: http://www.thunderlaser.com/laser-download

## Licensing
Distributed under the MIT license. See `LICENSE` for more information.
