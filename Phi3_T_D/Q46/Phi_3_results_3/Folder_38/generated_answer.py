def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[14] if 14 < len(nums) else 1
    num2 = nums[21] if 21 < len(nums) else 1
    num3 = nums[17] if 17 < len(nums) else 1
    return gcd(gcd(num1, num2), num3)