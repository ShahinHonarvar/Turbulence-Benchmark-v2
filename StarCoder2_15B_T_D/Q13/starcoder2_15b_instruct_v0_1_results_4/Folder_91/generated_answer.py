def find_second_largest_num(nums):
    nums_sorted = sorted(nums, reverse=True)
    if len(nums_sorted) >= 2:
        return nums_sorted[1]
    else:
        return None