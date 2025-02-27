from functools import reduce

def gcf_three_nums(nums):
    a = nums[85]
    b = nums[36]
    c = nums[54]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    def lcm_multiple(nums):
        return reduce(lcm, nums)
    lcm_abc = lcm_multiple([a, b, c])
    return lcm_abc // a // b // c