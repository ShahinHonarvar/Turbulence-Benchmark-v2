def gcf_two_nums(nums):
    gcf = nums[48]
    for i in range(48, 76):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf