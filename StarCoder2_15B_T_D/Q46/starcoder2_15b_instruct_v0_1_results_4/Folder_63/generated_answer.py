def gcf_three_nums(nums):
    gcf = nums[38]
    for i in range(39, 70):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf