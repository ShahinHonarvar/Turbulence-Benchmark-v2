def gcf_three_nums(nums):
    gcd = nums[412]
    for i in [932, 337]:
        while nums[i] != 0:
            gcd, nums[i] = (nums[i], gcd % nums[i])
    return gcd