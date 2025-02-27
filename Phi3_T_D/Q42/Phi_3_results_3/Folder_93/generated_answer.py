def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(nums):
    try:
        target_num = nums[45]
    except IndexError:
        return 'Index out of range'
    factors = set()
    divisor = 2
    while divisor <= target_num:
        if target_num % divisor == 0 and is_prime(divisor):
            factors.add(divisor)
            target_num //= divisor
        else:
            divisor += 1
    return factors