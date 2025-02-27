def find_second_largest_num(nums):
    max_num = nums[14]
    second_largest_num = None
    for i in range(15, 65):
        if nums[i] > max_num:
            second_largest_num = max_num
            max_num = nums[i]
        elif nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num