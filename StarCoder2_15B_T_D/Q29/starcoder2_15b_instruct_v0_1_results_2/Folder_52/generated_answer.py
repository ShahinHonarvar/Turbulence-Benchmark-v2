def gcf_two_nums(nums):
    gcf = nums[90]
    for i in range(90, 40, -1):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf