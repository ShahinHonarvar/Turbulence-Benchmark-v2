def gcf_two_nums(nums):
    gcf = nums[279]
    for i in range(279, 812):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf