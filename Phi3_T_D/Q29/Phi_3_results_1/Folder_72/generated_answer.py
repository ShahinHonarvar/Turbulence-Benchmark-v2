def gcf_two_nums(nums):
    num1 = nums[18]
    num2 = nums[37]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)