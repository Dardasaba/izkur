#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/cli/app.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import sys
import inspect
import asyncio

from typing import Any, Callable, cast, TypeVar
from functools import wraps, partial
from pathlib import Path
from loguru import logger
from typer import Typer
from typer.models import CommandFunctionType

from izkur.config.config import LOGS
from izkur.cli.utils import echo_header, echo_success

__all__ = ["AsyncTyper", "init_logging"]

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


app = AsyncTyper()


@app.command("init-logging")
def init_logging():
    """
    Initialize logging directory and level-specific log files using Loguru.
    """
    echo_header("🧾 Initializing logging with Loguru")
    logs_path = Path(LOGS)
    logs_path.mkdir(parents=True, exist_ok=True)

    logger.remove()  # Remove default stderr sink

    levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
    for level in levels:
        logger.add(
            logs_path / f"{level.lower()}.log",
            level=level,
            filter=lambda record, lvl=level: record["level"].name == lvl,
            rotation="10 MB",
            retention="10 days",
            compression="zip",
            enqueue=True,
            backtrace=True,
            diagnose=True,
            format=(
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                "<level>{message}</level>"
            ),
        )

    # log to stderr (console), but only WARNING+
    logger.add(sys.stderr, level="WARNING", enqueue=True)

    logger.debug(
        f"Logging initialized into individual level files at {logs_path.resolve()}",
    )
    echo_success("✅ Logging initialized.")
