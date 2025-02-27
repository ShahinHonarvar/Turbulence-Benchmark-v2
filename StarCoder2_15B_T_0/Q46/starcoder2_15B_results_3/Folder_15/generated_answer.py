def gcf_three_nums(nums):
    gcf = nums[4]
    for i in range(0, 8):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf