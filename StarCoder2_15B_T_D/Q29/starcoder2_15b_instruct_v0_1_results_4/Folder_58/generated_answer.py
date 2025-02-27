def gcf_two_nums(nums):
    gcf = nums[129]
    for i in range(129, 582):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf