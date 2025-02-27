def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 841 and len(nums) > 804:
        return gcd(nums[841], nums[804])
    else:
        raise IndexError('List is too short')