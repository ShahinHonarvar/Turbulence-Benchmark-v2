def gcf_three_nums(nums):
    gcf = nums[18]
    for i in range(10, 77):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf