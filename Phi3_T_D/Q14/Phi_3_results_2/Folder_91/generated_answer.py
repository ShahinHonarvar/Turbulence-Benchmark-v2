def find_second_smallest_num(nums):
    min_val = float('inf')
    second_min_val = float('inf')
    for i in range(6):
        if nums[i] < min_val:
            second_min_val = min_val
            min_val = nums[i]
        elif min_val < nums[i] < second_min_val:
            second_min_val = nums[i]
    return second_min_val if second_min_val < float('inf') else None