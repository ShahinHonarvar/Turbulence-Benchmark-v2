def find_second_largest_num(nums):
    sub_nums = nums[17:79]
    if len(sub_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None