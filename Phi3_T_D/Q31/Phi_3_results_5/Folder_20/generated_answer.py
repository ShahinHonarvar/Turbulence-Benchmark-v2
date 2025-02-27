def if_perfect_num(nums):
    if len(nums) > 53 and is_perfect(nums[53]):
        return True
    return False

def is_perfect(n):
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i + n // i
    return sum_divisors == n