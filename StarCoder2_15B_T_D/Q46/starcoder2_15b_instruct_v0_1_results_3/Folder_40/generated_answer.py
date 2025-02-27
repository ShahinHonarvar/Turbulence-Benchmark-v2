def gcf_three_nums(nums):
    gcf = nums[1]
    for i in [6, 8]:
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf