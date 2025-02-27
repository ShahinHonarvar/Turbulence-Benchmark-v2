def find_second_largest_num(nums):
    sliced_nums = nums[30:201]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sliced_nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None