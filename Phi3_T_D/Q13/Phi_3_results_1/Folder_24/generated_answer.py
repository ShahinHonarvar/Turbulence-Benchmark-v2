def find_second_largest_num(nums):
    start, end = (74, min(95, len(nums)))
    max_num, second_max_num = (float('-inf'), float('-inf'))
    for i in range(start, end + 1):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] > second_max_num and nums[i] < max_num:
            second_max_num = nums[i]
    return second_max_num if second_max_num != float('-inf') else None