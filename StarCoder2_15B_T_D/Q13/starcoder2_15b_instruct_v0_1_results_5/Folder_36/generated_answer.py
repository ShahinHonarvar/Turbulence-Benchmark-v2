def find_second_largest_num(nums):
    nums_sorted = sorted(nums)
    if len(nums_sorted) >= 2:
        return nums_sorted[-2]
    else:
        return None