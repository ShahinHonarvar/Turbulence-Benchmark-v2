def find_second_smallest_num(nums):
    min_val = float('inf')
    second_min_val = float('inf')
    relevant_range = nums[32:36]
    if len(relevant_range) < 2:
        return None
    for num in relevant_range:
        if num < min_val:
            second_min_val, min_val = (min_val, num)
        elif min_val < num < second_min_val:
            second_min_val = num
    return second_min_val