def gcf_two_nums(nums):
    return reduce(lambda x, y: gcd(x, y), [nums[0], nums[9]])