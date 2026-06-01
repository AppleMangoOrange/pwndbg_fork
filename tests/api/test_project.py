from __future__ import annotations

from pathlib import Path

import api

TEST_BINARY = Path("/bin/ls")


def test_project():
    proj = api.Project(TEST_BINARY)

    assert proj.binary_path == TEST_BINARY
    assert proj.arch is not None


def test_process():
    proj = api.Project(TEST_BINARY)
    proc = api.Process(proj)

    assert isinstance(proc, api.Process)
    assert proc.inferior is not None
