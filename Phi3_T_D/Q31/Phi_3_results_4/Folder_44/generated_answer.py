from math import sqrt

def if_perfect_num(nums):
    try:
        num_828 = nums[828]
        sum_divisors = sum((i for i in range(1, num_828) if num_828 % i == 0))
        return sum_divisors == num_828
    except IndexError:
        return False