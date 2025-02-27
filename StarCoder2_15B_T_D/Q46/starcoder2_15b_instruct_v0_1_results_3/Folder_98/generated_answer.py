def gcf_three_nums(nums):
    gcf = nums[8]
    for i in [2, 1]:
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf