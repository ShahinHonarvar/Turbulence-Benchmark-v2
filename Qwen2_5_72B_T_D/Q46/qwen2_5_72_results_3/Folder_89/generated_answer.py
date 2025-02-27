import math

def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    result = gcf(gcf(num1, num2), num3)
    return result