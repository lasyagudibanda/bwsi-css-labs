"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_all_pos_nums():
    nums = [1, 2, 3, 4, 5, 6, 7]
    assert max_subarray_sum(nums) == 28

def test_all_neg_nums():
    nums = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(nums) == 0

def test_mixed_nums():
    nums = [4, -1, -4, -5, 1, 2, 3, 2]
    assert max_subarray_sum(nums) == 8

def test_empty_set():
    nums = []
    assert max_subarray_sum(nums) == 0

if __name__ == "__main__":
    pytest.main()