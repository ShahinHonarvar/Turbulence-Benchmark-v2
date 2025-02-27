def find_second_largest_num(nums):
    if len(nums) < 89:
        return None
    sliced_nums = nums[22:89]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sliced_nums:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None