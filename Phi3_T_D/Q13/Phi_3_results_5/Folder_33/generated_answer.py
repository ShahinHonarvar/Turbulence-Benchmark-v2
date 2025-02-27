def find_second_largest_num(nums):
    if not 667 <= len(nums) <= 774:
        return None
    sliced_nums = nums[667:775]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sliced_nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None