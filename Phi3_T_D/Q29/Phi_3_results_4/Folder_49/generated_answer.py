def gcf_two_nums(nums):
    a = nums[28 % len(nums)]
    b = nums[20 % len(nums)]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(a, b)