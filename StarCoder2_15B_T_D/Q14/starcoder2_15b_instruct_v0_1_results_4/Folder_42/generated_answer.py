def find_second_smallest_num(nums):
    nums_sorted = sorted(nums)
    second_smallest = nums_sorted[21]
    if 21 <= len(nums_sorted) - 1:
        return second_smallest
    else:
        return None