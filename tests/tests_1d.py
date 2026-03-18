"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_all_pos_nums():
    nums = [1, 2, 3, 4, 12, 15, 7]
    assert two_sum(nums, 9) == [1, 6]

def test_all_neg_nums():
    nums = [-1, -2, -3, -4, -7]
    assert two_sum(nums, -6) == [1, 3]

def test_mixed_nums():
    nums = [4, -1, -4, -5, 1, 2, 3, 2]
    assert two_sum(nums, 0) == [0, 2]


if __name__ == "__main__":
    pytest.main()