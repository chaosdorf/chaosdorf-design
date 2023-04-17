import pathlib
import os.path
import sys
from typing import Optional

from palettelib.format.format_ase import PaletteFormatASE
from palettelib.format.format_gpl import PaletteFormatGPL
from palettelib.format.format_kpl import PaletteFormatKPL
from palettelib.format.format_yaml import PaletteFormatYAML
from palettelib.io import PaletteFormat, PaletteReader, PaletteWriter
from palettelib.palette import Palette

formats: list[PaletteFormat] = [PaletteFormatYAML, PaletteFormatGPL, PaletteFormatASE, PaletteFormatKPL]
readers: dict[str, PaletteReader] = dict([(format, reader) for format, reader, writer in formats])
writers: dict[str, PaletteWriter] = dict([(format, writer) for format, reader, writer in formats])

formats = [PaletteFormatYAML, PaletteFormatGPL, PaletteFormatASE, PaletteFormatKPL]
readers = dict([(format, reader) for format, reader, writer in formats])
writers = dict([(format, writer) for format, reader, writer in formats])


def read_file(filepath: str) -> Palette:
    reader: Optional[PaletteReader] = None
    for format in readers:
        if filepath.endswith(format):
            reader = readers.get(format)
    if reader is None:
        raise Exception("unrecognized format: {0}".format(filepath))
    return reader(filepath)


def write_file(filepath: str, data: Palette):
    writer: Optional[PaletteWriter] = None
    for format in writers:
        if filepath.endswith(format):
            writer = writers.get(format)
    if writer is None:
        raise Exception("unrecognized format: {0}".format(filepath))
    return writer(filepath, data)


def convert(filepath: str):
    suffix = ""
    for format in readers:
        if filepath.endswith(format):
            suffix = format
    data = read_file(filepath)
    name = os.path.basename(filepath)[:-len(suffix)]
    dirname = os.path.dirname(filepath)
    for format in writers:
        if filepath.endswith(format):
            continue
        write_file(os.path.join(dirname, "{0}{1}".format(name, format)), data)


def main():
    filepaths = sys.argv[1:]
    for filepath in filepaths:
        convert(filepath)


if __name__ == "__main__":
    main()
