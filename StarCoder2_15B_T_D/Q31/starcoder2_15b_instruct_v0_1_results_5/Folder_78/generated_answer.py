import math

def if_perfect_num(nums):
    if not isinstance(nums, list):
        return False
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        return False

    def is_perfect_num(n):
        sum_of_divisors = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                sum_of_divisors += i
                if i != 1 and i != n // i:
                    sum_of_divisors += n // i
        return sum_of_divisors == n
    return is_perfect_num(nums[91])