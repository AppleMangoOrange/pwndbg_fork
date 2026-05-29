from pathlib import Path

import pytest

import pwndbg
import api

TEST_BINARY = Path("/bin/ls")

@pytest.mark.integration
async def test_project():
    proj = api.Project(TEST_BINARY)

    assert proj.binary_path == TEST_BINARY
    assert proj.arch is not None

@pytest.mark.integration
async def test_process():
    proj = api.Project(TEST_BINARY)
    proc = proj.run()

    assert isinstance(proc, api.Process)
    assert not isinstance(proc.inferior, none)
