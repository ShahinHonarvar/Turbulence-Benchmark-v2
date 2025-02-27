def find_second_largest_num(nums):
    start, end = (min(100, len(nums)), min(201, len(nums)))
    if start >= end:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in nums[start:end + 1]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None