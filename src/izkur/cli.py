#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/cli.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import sys

from pathlib import Path
from babel import Locale
from loguru import logger
from rich.console import Console

from izkur import LOGS, AsyncTyper, echo_header, echo_success

locale = Locale("he", "IL")
locale.territories["IL"]

app = AsyncTyper()
console = Console()
if sys.platform == "win32":
    console = Console(force_terminal=True, legacy_windows=True)


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


@app.command("run-all")
async def run_all():
    init_logging()


if __name__ == "__main__":
    app()
