def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_of_three(nums[62], nums[96], nums[26])