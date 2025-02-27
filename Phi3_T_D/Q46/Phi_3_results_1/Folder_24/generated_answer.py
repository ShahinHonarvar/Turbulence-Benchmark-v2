def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 18 in range(len(nums)) and 37 in range(len(nums)) and (43 in range(len(nums))):
        return gcd(gcd(nums[18], nums[37]), nums[43])
    else:
        return None