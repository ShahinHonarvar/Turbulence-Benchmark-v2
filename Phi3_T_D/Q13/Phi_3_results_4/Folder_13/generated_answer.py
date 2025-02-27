def find_second_largest_num(nums):
    target_range = nums[25:88]
    if len(target_range) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in target_range:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None