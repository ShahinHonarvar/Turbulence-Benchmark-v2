def find_second_smallest_num(nums):
    if len(nums) < 15:
        return None
    start_idx, end_idx = (70, 84)
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(start_idx, end_idx + 1):
        if nums[i] < min_num:
            min_num = nums[i]
        elif nums[i] < second_min_num and nums[i] != min_num:
            second_min_num = nums[i]
    return second_min_num if second_min_num != float('inf') else None