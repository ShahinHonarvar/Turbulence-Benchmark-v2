def gcf_three_nums(nums):
    gcf = nums[41]
    for n in nums[42:70]:
        gcf = max(gcf, n)
    for n in nums[29:41] + nums[70:]:
        gcf = max(gcf, n)
    return gcf