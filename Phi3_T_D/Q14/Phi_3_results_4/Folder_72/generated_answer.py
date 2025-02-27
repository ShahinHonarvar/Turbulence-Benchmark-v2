def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    start, end = (82, min(86, len(nums)))
    min_num = float('inf')
    second_min_num = None
    for i in range(start, end + 1):
        if nums[i] < min_num:
            min_num, second_min_num = (nums[i], min_num)
        elif second_min_num is None or nums[i] < second_min_num:
            second_min_num = nums[i]
    return second_min_num