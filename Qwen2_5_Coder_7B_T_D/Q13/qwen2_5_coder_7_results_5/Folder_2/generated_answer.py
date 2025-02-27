def find_second_largest_num(nums):
    if len(nums) < 30:
        return None
    subset = nums[15:40]
    if len(subset) < 2:
        return None
    first, second = (subset[0], subset[1]) if subset[0] > subset[1] else (subset[1], subset[0])
    for num in subset[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != first else None