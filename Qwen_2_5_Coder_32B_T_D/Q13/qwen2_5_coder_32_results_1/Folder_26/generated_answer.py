def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    sublist = nums[62:100]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None