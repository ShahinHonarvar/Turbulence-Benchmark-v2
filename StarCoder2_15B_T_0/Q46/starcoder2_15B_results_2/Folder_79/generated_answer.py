def gcf_three_nums(nums):
    gcf = nums[16]
    for i in range(17, 96):
        gcf = gcd(gcf, nums[i])
    return gcf