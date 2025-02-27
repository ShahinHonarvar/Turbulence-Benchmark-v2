def find_second_smallest_num(nums):
    nums_sorted = sorted(nums)
    if len(nums_sorted) >= 20:
        return nums_sorted[19]
    else:
        return None