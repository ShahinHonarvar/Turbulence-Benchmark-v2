def gcf_three_nums(nums):
    gcf = nums[21]
    for i in (21, 51, 33):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf