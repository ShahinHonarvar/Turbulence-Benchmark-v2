def gcf_two_nums(nums):
    a = nums[90]
    b = nums[54]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(a, b)