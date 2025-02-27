def find_second_smallest_num(nums):
    if len(nums) < 41:
        return None
    sub_list = nums[28:41]
    if len(sub_list) < 2:
        return None
    min_val = float('inf')
    second_min_val = float('inf')
    for num in sub_list:
        if num < min_val:
            second_min_val = min_val
            min_val = num
        elif min_val < num < second_min_val:
            second_min_val = num
    return second_min_val if second_min_val != float('inf') else None