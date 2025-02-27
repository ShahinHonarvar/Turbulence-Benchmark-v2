def gcf_three_nums(nums):
    gcf = nums[307]
    for i in range(308, 921):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf