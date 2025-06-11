#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/cli/utils.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import typer

__all__ = [
    "echo_info",
    "echo_success",
    "echo_warning",
    "echo_error",
    "echo_header",
]


def echo_info(msg: str) -> None:
    typer.secho(msg, fg="cyan")


def echo_success(msg: str) -> None:
    typer.secho(msg, fg="green", bold=True)


def echo_warning(msg: str) -> None:
    typer.secho(msg, fg="yellow", bold=True)


def echo_error(msg: str) -> None:
    typer.secho(msg, fg="red", bold=True, err=True)


def echo_header(msg: str) -> None:
    typer.secho(msg, fg="magenta", bold=True, underline=True)
