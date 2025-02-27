def gcf_three_nums(nums):
    gcf = nums[74]
    for i in range(73, 19, -1):
        if nums[i] > 0 and gcf % nums[i] == 0:
            gcf = nums[i]
            break
    return gcf