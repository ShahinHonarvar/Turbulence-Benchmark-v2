def gcf_three_nums(nums):
    gcf = nums[7]
    for i in range(6, 8):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf