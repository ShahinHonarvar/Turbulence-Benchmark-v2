def find_largest_num(nums):
    largest_num = nums[62]
    for num in nums[62:93]:
        if num > largest_num:
            largest_num = num
    return largest_num