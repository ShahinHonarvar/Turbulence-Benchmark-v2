def find_second_smallest_num(nums):
    nums_subset = sorted(nums[56:83])
    if len(nums_subset) < 2:
        return None
    return nums_subset[1]