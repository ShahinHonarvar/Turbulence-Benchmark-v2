def find_second_smallest_num(nums):
    nums_subset = nums[639:976]
    nums_sorted = sorted(nums_subset)
    if len(nums_sorted) >= 2:
        return nums_sorted[1]
    else:
        return None