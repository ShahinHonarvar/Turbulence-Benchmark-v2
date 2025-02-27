def gcf_three_nums(nums):
    gcf = nums[7]
    for i in range(8, 10):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf