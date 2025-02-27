def if_perfect_num(nums):
    if len(nums) > 15 and is_perfect(nums[15]):
        return True
    return False

def is_perfect(n):
    sum_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_divisors == n