# test_average_calculator.py

import pytest
from average_calculator import calculate_average

def test_average_pass():
    numbers = [10, 20, 30, 40, 50]
    assert calculate_average(numbers) == 30.0  # This test will pass

def test_average_fail():
    numbers = [10, 20, 30]
    assert calculate_average(numbers) == 40.0  # This test will fail (average is 20.0)