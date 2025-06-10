#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/helpers/cli_utils.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import inspect
import asyncio
import typer

from typing import Any, Callable, cast, TypeVar
from functools import wraps, partial
from typer import Typer
from typer.models import CommandFunctionType

__all__ = [
    "AsyncTyper",
    "echo_info",
    "echo_success",
    "echo_warning",
    "echo_error",
    "echo_header",
]

T = TypeVar("T")


class AsyncTyper(Typer):
    @staticmethod
    def maybe_run_async(
        decorator: Callable[[CommandFunctionType], CommandFunctionType],
        func: CommandFunctionType,
    ) -> CommandFunctionType:
        if inspect.iscoroutinefunction(func):

            @wraps(func)
            def runner(*args: Any, **kwargs: Any) -> Any:
                return asyncio.run(func(*args, **kwargs))

            decorator(cast(CommandFunctionType, runner))
        else:
            decorator(func)
        return func

    def callback(self, *args: Any, **kwargs: Any) -> Any:
        decorator = super().callback(*args, **kwargs)
        return partial(self.maybe_run_async, decorator)

    def command(self, *args: Any, **kwargs: Any) -> Any:
        decorator = super().command(*args, **kwargs)
        return partial(self.maybe_run_async, decorator)


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
