def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    try:
        x, y, z = (nums[742], nums[888], nums[629])
        return gcd(gcd(x, y), z)
    except IndexError:
        return None