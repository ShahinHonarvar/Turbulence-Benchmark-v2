def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 872 < len(nums) and 219 < len(nums):
        return gcd(nums[872], nums[219])
    else:
        return None