def gcf_three_nums(nums):
    gcf = nums[0]
    for i in range(1, len(nums)):
        gcf = math.gcd(gcf, nums[i])
    return gcf