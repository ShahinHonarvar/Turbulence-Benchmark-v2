def gcf_three_nums(nums):
    gcf = nums[76]
    for i in range(35, 75):
        gcf = gcd(gcf, nums[i])
    return gcf