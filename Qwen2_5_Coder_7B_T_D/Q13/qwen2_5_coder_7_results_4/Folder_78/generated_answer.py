def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sub_nums = nums[43:52]
    if len(sub_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None