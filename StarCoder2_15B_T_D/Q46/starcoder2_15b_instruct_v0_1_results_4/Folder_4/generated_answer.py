def gcf_three_nums(nums):
    gcf = nums[24]
    for i in range(25, 81):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf