
import pytest

@pytest.mark.slow
def test_slow_process():
    # Your slow test logic here
    assert True

def test_fast_process():
    # A fast test
    assert True


