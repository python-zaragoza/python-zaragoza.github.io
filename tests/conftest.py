"""Tests - Conftest."""

import pytest


@pytest.fixture
def project_name() -> str:
    """Project name fixture.

    Returns:
        str: String containing the project name.

    """
    return "Python Zaragoza Site"
