def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < max(404, 834, 517):
        return None
    return gcd(gcd(nums[404], nums[834]), nums[517])