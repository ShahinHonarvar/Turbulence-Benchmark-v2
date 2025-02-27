from itertools import islice

def find_second_largest_num(nums):
    sliced_list = islice(nums, 5, 8)
    try:
        return sorted(set(sliced_list))[-2]
    except IndexError:
        return None