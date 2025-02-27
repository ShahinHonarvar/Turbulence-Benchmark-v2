def gcf_three_nums(nums):
    num1 = nums[85] if len(nums) > 85 else None
    num2 = nums[36] if len(nums) > 36 else None
    num3 = nums[54] if len(nums) > 54 else None
    if None in [num1, num2, num3]:
        return None

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    common_factor = gcd(num1, gcd(num2, num3))
    return common_factor