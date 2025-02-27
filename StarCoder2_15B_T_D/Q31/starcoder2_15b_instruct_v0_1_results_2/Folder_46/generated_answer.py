def if_perfect_num(nums):
    return is_perfect_num(nums[453])

def is_perfect_num(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num