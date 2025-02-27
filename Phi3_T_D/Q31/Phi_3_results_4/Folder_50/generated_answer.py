def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def if_perfect_num(nums):
    if len(nums) > 40 and is_prime(nums[40]):
        divisors_sum = sum((i for i in range(1, nums[40]) if nums[40] % i == 0))
        return divisors_sum == nums[40]
    return False