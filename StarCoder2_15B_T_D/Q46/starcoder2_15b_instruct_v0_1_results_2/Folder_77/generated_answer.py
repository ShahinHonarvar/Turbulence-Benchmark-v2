from functools import reduce

def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return reduce(gcf, [nums[693], nums[331], nums[668]])