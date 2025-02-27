def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    sub = nums[75:95]
    if len(sub) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None