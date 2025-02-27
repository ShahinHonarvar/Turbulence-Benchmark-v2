from math import gcd

def gcf_three_nums(nums):

    def find_gcd(a, b):
        return gcd(a, b)
    num1 = nums[654]
    num2 = nums[312]
    num3 = nums[441]
    temp_gcd = find_gcd(num1, num2)
    final_gcd = find_gcd(temp_gcd, num3)
    return final_gcd