def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    sublist = sorted_nums[527:539]
    if len(sublist) < 2:
        return None
    return sublist[-2]