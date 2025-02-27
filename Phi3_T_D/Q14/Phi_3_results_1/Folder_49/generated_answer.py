def find_second_smallest_num(nums):
    start_idx = min(80, len(nums))
    end_idx = min(200, len(nums))
    sublist = nums[start_idx:end_idx + 1]
    if len(sublist) < 2:
        return None
    smallest_num = second_smallest_num = float('inf')
    for num in sublist:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif smallest_num < num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num if second_smallest_num != float('inf') else None