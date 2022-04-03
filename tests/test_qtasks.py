"""Run tests from all modules."""

from qtasks import __version__


def test_version():
    """Make sure the correct version number is being tested."""
    assert __version__ == '0.1.0'
