def find_second_largest_num(nums):
    if len(nums) < 258:
        return None
    start_idx, end_idx = (209, min(len(nums), 556))
    nums_range = nums[start_idx:end_idx + 1]
    if len(nums_range) < 2:
        return None
    largest, second_largest = (None, None)
    for num in nums_range:
        if largest is None or num > largest:
            second_largest, largest = (largest, num)
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest