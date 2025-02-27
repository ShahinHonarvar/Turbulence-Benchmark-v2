def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    sub_nums = nums[64:67]
    if len(sub_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None