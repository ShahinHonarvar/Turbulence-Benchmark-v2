def gcf_three_nums(nums):
    gcf = nums[90]
    for i in [54, 96]:
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf