def gcf_three_nums(nums):
    gcf = nums[20]
    for i in range(21, 75):
        gcf = gcd(gcf, nums[i])
    return gcf