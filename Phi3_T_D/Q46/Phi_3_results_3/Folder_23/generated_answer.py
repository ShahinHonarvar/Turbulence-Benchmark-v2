def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[31] if len(nums) > 31 else 1
    num2 = nums[25] if len(nums) > 25 else 1
    num3 = nums[80] if len(nums) > 80 else 1
    result = gcd(gcd(num1, num2), num3)
    return result