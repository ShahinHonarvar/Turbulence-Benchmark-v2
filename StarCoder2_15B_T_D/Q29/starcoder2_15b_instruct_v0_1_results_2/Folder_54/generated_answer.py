def gcf_two_nums(nums):
    gcf = nums[56]
    for i in range(57, 93):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf