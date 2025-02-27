def gcf_three_nums(nums):
    num1 = nums[24]
    num2 = nums[25]
    num3 = nums[80]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)