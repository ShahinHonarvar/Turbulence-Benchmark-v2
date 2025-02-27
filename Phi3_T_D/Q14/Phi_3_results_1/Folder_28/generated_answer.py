def find_second_smallest_num(nums):
    relevant = nums[22:51]
    if len(relevant) < 2:
        return None
    second_min = float('inf')
    min_num = float('inf')
    for num in relevant:
        if num < min_num:
            min_num, second_min = (num, min_num)
        elif min_num < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None