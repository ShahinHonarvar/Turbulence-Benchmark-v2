def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 33 and len(nums) > 85:
        return gcd(nums[85], nums[33])
    else:
        return None