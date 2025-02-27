def gcf_two_nums(nums):
    num1 = nums[95]
    num2 = nums[85]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    gcf = gcd(num1, num2)
    return gcf