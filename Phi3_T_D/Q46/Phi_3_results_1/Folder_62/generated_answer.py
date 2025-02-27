def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_of_three(nums[10], nums[55], nums[36])