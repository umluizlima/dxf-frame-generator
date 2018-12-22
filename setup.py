from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dxf-frame-generator",
    version="0.0.1",
    author="Luiz Lima",
    author_email="umluizlima@gmail.com",
    license="MIT License",
    description="Custom sized frames for digital fabrication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umluizlima/dxf-frame-generator",
    py_modules=['dxf_frame_generator'],
    install_requires=['ezdxf'],
    entry_points={
        'console_scripts': [
            'dxf-frame-generator=dxf_frame_generator:run',
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
