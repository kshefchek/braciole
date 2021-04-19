#!/usr/bin/env python3

import logging

import typer

from koza.koza_runner import transform_source, validate_file
from koza.model.config.source_config import CompressionType, FormatType

app = typer.Typer()


logging.basicConfig()
LOG = logging.getLogger(__name__)


@app.command()
def transform(
    source: str = typer.Option(..., help="Source name"),
    config_dir: str = typer.Option('./', help="Path to configuration directory"),
    output_dir: str = typer.Option('./output', help="Path to output directory"),
    curie_map: str = typer.Option(None, help="Path to custom curie map file"),
    quiet: bool = False,
    debug: bool = False,
):
    """
    Run Koza
    """
    _set_log_level(quiet, debug)

    transform_source(source, config_dir, output_dir, curie_map)


@app.command()
def validate(
    file: str = typer.Option(..., help="Path or url to the source file"),
    format: FormatType = FormatType.csv,
    delimiter: str = ',',
    header_delimiter: str = None,
    compression: CompressionType = None,
    skip_lines: int = 0,
    skip_blank_lines: bool = True,
):
    """
    Run a single file through koza
    """
    _set_log_level(debug=True)

    validate_file(
        file, format, delimiter, header_delimiter, compression, skip_lines, skip_blank_lines
    )


@app.command()
def create():
    """
    TODO
    Create a new koza project
    """


def _set_log_level(quiet: bool = False, debug: bool = False):
    if quiet:
        logging.getLogger().setLevel(logging.WARNING)
    elif debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)


if __name__ == "__main__":
    app()
