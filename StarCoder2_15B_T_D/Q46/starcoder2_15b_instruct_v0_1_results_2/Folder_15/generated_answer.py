def gcf_three_nums(nums):
    gcf = nums[4]
    for i in range(0, 9):
        if i != 4:
            gcf = max(gcf, nums[i])
    return gcf