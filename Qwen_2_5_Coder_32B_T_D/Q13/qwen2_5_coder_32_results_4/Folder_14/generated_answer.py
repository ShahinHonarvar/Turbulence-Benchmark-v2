def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    subset = nums[5:8]
    if len(subset) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in subset:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None