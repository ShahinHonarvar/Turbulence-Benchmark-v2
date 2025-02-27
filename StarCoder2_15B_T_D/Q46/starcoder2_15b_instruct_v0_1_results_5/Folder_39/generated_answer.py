def gcf_three_nums(nums):
    gcf = nums[85]
    for i in range(86, 55, -1):
        if nums[i] % gcf == 0 and nums[36] % gcf == 0 and (nums[54] % gcf == 0):
            return gcf
    gcf -= 1
    return gcf