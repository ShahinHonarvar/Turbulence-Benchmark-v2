def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    slice = nums[50:55]
    if len(slice) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in slice:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None