def gcf_three_nums(nums):
    gcf = nums[27]
    for i in [85, 51]:
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf