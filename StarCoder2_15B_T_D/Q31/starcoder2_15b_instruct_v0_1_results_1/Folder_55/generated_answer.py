import math

def if_perfect_num(nums):
    if len(nums) < 22:
        return False
    num = nums[21]
    sum_of_divisors = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != 1 and i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num