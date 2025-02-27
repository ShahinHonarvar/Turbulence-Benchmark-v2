def gcf_three_nums(nums):
    gcf = nums[74]
    for i in range(73, 26, -1):
        while nums[i] % gcf != 0:
            gcf -= 1
    for i in range(50, 26, -1):
        while nums[i] % gcf != 0:
            gcf -= 1
    for i in range(26, 0, -1):
        while nums[i] % gcf != 0:
            gcf -= 1
    return gcf