import pytest
import os
import random


def binary_search(my_list, item: int):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def test_binary_search():
    the_list = range(1, 101)
    the_item = random.randint(1, 101)
    assert binary_search(the_list, the_item) == the_list.index(the_item)


if __name__ == '__main__':
    pytest.main(['-x', '-s', os.path.realpath(__file__)])
