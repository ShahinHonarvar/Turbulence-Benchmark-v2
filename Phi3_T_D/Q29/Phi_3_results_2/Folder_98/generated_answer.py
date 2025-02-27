def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 9 and len(nums) > 0:
        return gcd(nums[0], nums[9])
    else:
        return None