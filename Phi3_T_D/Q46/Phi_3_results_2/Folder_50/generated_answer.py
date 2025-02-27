def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[20]
    num2 = nums[35]
    num3 = nums[74]
    return gcd(num1, gcd(num2, num3))