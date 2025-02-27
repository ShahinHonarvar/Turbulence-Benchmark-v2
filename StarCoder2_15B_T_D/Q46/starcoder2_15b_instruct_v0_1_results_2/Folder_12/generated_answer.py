def gcf_three_nums(nums):
    gcf = nums[91]
    for i in range(91, 44, -1):
        if nums[i] % gcf == 0 and nums[45] % gcf == 0 and (nums[48] % gcf == 0):
            return gcf
    return gcf