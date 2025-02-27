def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    while num:
        if not is_prime(num) or '0' in str(num):
            return False
        num = int(str(num)[1:])
    return True

def all_left_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)