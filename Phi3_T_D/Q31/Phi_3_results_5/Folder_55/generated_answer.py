def if_perfect_num(nums):
    if len(nums) > 21 and is_perfect_number(nums[21]):
        return True
    return False

def is_perfect_number(n):
    sum_of_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
        i += 1
    return sum_of_divisors == n and n != 1