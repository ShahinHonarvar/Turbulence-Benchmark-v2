def gcf_three_nums(nums):
    gcf = nums[8]
    for i in range(7, -1, -1):
        if nums[i] < gcf:
            gcf = nums[i]
    return gcf