def gcf_three_nums(nums):
    gcf = nums[19]
    for i in range(20, 80, 25):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf