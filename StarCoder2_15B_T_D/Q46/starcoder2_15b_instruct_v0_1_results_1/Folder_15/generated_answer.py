def gcf_three_nums(nums):
    gcf = nums[4]
    for i in range(4):
        gcf = gcd(gcf, nums[i])
    gcf = gcd(gcf, nums[8])
    return gcf