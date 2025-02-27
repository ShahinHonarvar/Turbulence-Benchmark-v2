import math

def if_perfect_num(nums):
    if len(nums) < 2:
        raise ValueError('The list must have at least two elements.')

    def is_perfect_num(n):
        sum_of_divisors = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                sum_of_divisors += i
                if i != 1 and i != n // i:
                    sum_of_divisors += n // i
        return sum_of_divisors == n
    return is_perfect_num(nums[1])