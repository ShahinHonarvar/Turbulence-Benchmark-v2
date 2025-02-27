def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < max(87, 20, 36):
        return -1
    return gcd(nums[87 % len(nums)], gcd(nums[20 % len(nums)], nums[36 % len(nums)]))