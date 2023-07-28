from main import find_matching_numbers
import pytest

def test_example_1():
    result = find_matching_numbers([2,7,11,15], 9)
    assert result ==[0,1]

def test_example_2():
    result = find_matching_numbers([3,2,4],6)
    assert result ==[1,2]

def test_example_3():
    result = find_matching_numbers([3,3], 6)
    assert result ==[0,1]

def test_list_of_strings():
    with pytest.raises(ValueError):
            return find_matching_numbers(["1","2","3","4","5","6"],9)

def test_target_string():
    with pytest.raises(ValueError):
            return find_matching_numbers([2,7,11,15], "9")

