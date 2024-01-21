
import pytest
import my_plugin_hookspec

# Adding the custom hook to Pytest
def pytest_addhooks(pluginmanager):
    pluginmanager.add_hookspecs(my_plugin_hookspec)

# Implementation of the custom hook
@pytest.hookimpl
def pytest_my_custom_hook():
    print("Custom hook called from the test file.")
