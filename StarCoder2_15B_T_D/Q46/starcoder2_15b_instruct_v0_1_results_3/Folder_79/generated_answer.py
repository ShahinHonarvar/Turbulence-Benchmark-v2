from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('nums must have at least three elements')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('nums must only contain positive integers')

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return reduce(gcf, [nums[16], nums[87], nums[95]])