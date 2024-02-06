import pytest


@pytest.hookimpl()
def pytest_my_hook(config):
    print("Hello from `pytest_my_hook` hook!")
    print(f"Config: {config}")
