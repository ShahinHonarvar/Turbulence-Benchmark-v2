def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 412 < len(nums) and 932 < len(nums) and (337 < len(nums)):
        result = gcd(gcd(nums[412], nums[932]), nums[337])
        return result
    raise IndexError('Index out of range')