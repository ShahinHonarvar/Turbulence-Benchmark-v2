def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def if_perfect_num(nums):
    if len(nums) > 247 and is_prime(247):
        num = nums[247]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False