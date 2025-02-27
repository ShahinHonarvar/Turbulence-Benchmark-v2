def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    if not is_prime(num):
        return False
    return is_left_right_truncatable_prime(num // 10) and is_left_right_truncatable_prime(num % 100)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True