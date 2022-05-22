from typing import Union


def get_sum_from_lists(lists: list) -> Union[int, float]:
    """Returns sum of all elements from given list"""
    nums = []
    for number in lists:
        if not isinstance(number, list):
            nums.append(number)
        else:
            nums.append(get_sum_from_lists(number))
    return sum(nums)
