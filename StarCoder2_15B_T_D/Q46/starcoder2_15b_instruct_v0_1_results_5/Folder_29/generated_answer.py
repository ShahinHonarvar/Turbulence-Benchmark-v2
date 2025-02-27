def gcf_three_nums(nums):
    return gcd(nums[22], nums[97], nums[64])

def gcd(*numbers):

    def _gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(numbers) == 2:
        return _gcd(numbers[0], numbers[1])
    else:
        return _gcd(numbers[0], gcd(*numbers[1:]))