def find_second_largest_num(nums):
    slice_nums = nums[12:93]
    if len(slice_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in slice_nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None