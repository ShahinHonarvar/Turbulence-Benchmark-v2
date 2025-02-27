def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1 = nums[47]
    n2 = nums[10]
    n3 = nums[28]
    result = gcd(n1, gcd(n2, n3))
    return result