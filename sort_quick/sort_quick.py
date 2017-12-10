import pytest
import os
import random


def quick_sort(my_list: list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    less = []
    more = []
    equal = []
    for item in my_list:
        if item < pivot:
            less.append(item)
        if item > pivot:
            more.append(item)
        if item == pivot:
            equal.append(item)
    return quick_sort(less) + equal + quick_sort(more)


def test_quick_sort():
    the_list = [random.randint(-500, 501) for item in range(1, 10)]
    assert quick_sort(the_list) == sorted(the_list)


if __name__ == '__main__':
    pytest.main(['-x', '-s', os.path.realpath(__file__)])
