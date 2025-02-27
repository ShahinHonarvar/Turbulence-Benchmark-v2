def gcf_three_nums(nums):
    gcf = nums[9]
    for i in range(9, 6, -1):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf