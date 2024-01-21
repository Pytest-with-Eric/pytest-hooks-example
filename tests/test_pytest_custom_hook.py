
def test_direct_hook_call():
    from conftest import pytest_my_custom_hook  # Import the hook

    pytest_my_custom_hook()  # Directly call the hook
    assert True