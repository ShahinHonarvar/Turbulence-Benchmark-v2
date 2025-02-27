def find_second_largest_num(nums):
    start, end = (40, 80)
    if end >= len(nums):
        return None
    second_largest = float('-inf')
    max_num = float('-inf')
    for i in range(start, end + 1):
        if nums[i] > max_num:
            second_largest = max_num
            max_num = nums[i]
        elif nums[i] > second_largest and nums[i] != max_num:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None