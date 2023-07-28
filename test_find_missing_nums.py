from main import find_missing_nums
import pytest

def test_example_1():
    result = find_missing_nums([4,3,2,7,8,2,3,1])
    assert result ==[5,6]

def test_example_2():
    result = find_missing_nums([1,1])
    assert result ==[2]

def test_not_missing_numbers():
    result = find_missing_nums([1,2,3,4,5,6])
    assert result ==[]

def test_list_of_strings():
    with pytest.raises(ValueError):
            return find_missing_nums(["1","2","3","4","5","6"])