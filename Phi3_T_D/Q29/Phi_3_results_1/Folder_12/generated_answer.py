def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_56 = nums[56] if len(nums) > 56 else None
    index_54 = nums[54] if len(nums) > 54 else None
    if index_56 is None or index_54 is None:
        return None
    return gcd(index_56, index_54)