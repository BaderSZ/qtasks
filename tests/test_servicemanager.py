"""Test service manager."""

# import pytest
from qtasks.manager.servicemanager import ServiceManager


def test_servicemanager_init():
    """Make sure initialised object is empty."""
    servicemanager = ServiceManager()
    assert servicemanager.credentials is None
    assert servicemanager.service is None


# def test_servicemanager_wrongkey():
#     """TODO."""
#     servicemanager = ServiceManager()

#     with pytest.raises(OSError):
#         servicemanager.create("emptykey.json")
