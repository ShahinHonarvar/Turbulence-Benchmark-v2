def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 889 or len(nums) < 743 or len(nums) < 630:
        raise ValueError('The list must have at least 889 elements')
    first_gcd = gcd(nums[888], nums[742])
    final_gcd = gcd(first_gcd, nums[629])
    return final_gcd