
import os
import pytest

def pytest_collection_modifyitems(config, items):
    if os.getenv('RUN_SLOW_TESTS') != '1':
        # Skip slow tests if the environment variable is not set
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
