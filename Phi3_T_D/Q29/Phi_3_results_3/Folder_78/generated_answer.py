def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 13 or len(nums) < 54:
        return 'Invalid list size'
    return gcd(nums[54], nums[13])