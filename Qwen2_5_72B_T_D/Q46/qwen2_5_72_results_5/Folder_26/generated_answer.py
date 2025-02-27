from math import gcd

def gcf_three_nums(nums):

    def find_gcf(x, y):
        return gcd(x, y)
    num1 = nums[15]
    num2 = nums[51]
    num3 = nums[76]
    temp_gcf = find_gcf(num1, num2)
    final_gcf = find_gcf(temp_gcf, num3)
    return final_gcf