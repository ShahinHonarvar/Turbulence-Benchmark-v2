def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    sublist = nums[62:93]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None