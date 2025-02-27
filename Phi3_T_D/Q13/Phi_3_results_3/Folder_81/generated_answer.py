def find_second_largest_num(nums):
    if len(nums) < 2 or max(nums) is nums[0]:
        return None
    start = max(10, min(len(nums), 100))
    first, second = (float('-inf'), float('-inf'))
    for num in nums[start:min(start + 1, len(nums))]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None