def if_perfect_num(nums):
    if len(nums) > 28 and is_perfect(nums[28]):
        return True
    return False

def is_perfect(num):
    if num < 2:
        return False
    divisors = sum([i for i in range(1, num // 2 + 1) if num % i == 0])
    return divisors == num