def find_second_largest_num(nums):
    max_num = float('-inf')
    second_largest_num = float('-inf')
    for i in range(28, 33):
        if nums[i] > max_num:
            second_largest_num = max_num
            max_num = nums[i]
        elif nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num if second_largest_num != float('-inf') else None