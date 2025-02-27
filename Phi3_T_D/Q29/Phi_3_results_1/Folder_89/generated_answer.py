def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    return gcd(nums[37], nums[30])