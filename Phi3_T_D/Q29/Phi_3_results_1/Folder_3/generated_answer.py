def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 47 < len(nums) and 10 < len(nums):
        return gcd(nums[47], nums[10])
    return None