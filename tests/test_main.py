"""
test_main
----------------------------------
Tests for `main` module.
"""
from tfx_stuff import main


def test_main():
    assert main.main() == 'hello'
