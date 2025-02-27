def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[91], nums[45]) + 1):
        if nums[91] % i == 0 and nums[45] % i == 0:
            gcf = i
    return gcf