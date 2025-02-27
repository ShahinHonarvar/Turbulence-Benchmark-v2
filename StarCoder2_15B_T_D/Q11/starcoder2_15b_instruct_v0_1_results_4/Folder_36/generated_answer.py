def find_largest_num(nums):
    largest_num = nums[246]
    for i in range(247, 751):
        if nums[i] > largest_num:
            largest_num = nums[i]
    return largest_num