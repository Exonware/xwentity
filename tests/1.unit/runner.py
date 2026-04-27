#!/usr/bin/env python3
"""
#exonware/xwentity/tests/1.unit/runner.py
Unit test runner for xwentity
Orchestrates all unit test module runners.
Company: eXonware.com
Author: eXonware Backend Team
Email: connect@exonware.com
Version: 0.0.1.0
Generation Date: 28-Jan-2026
"""

import sys
import os
from pathlib import Path

from exonware.xwsystem.console.cli import ensure_utf8_console

ensure_utf8_console()


def _package_root() -> Path:
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "pyproject.toml").is_file() and (p / "src").is_dir():
            return p
        p = p.parent
    raise RuntimeError("Could not locate package root from " + str(Path(__file__)))


_PKG_ROOT = _package_root()

from exonware.xwsystem.utils.test_runner import TestRunner


def main() -> int:
    """Run unit tests."""
    os.chdir(_PKG_ROOT)
    runner = TestRunner(
        library_name="xwentity",
        layer_name="1.unit",
        description="Unit Tests - Component Tests",
        test_dir=Path(__file__).parent,
        pytest_cwd=_PKG_ROOT,
        markers=["xwentity_unit"],
    )
    return runner.run()


if __name__ == "__main__":
    sys.exit(main())
