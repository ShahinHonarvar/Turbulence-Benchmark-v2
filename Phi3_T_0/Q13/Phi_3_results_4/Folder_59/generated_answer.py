def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 10:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None