def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first = gcd(nums[31], nums[69])
    result = gcd(first, nums[40])
    return result