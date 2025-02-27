from functools import reduce

def gcf_two_nums(nums):
    num1 = nums[88]
    num2 = nums[35]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return reduce(gcf, [num1, num2])