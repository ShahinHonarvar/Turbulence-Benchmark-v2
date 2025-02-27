def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    digits = [int(d) for d in str(num)]
    if 0 in digits:
        return False
    while len(digits) > 1:
        digits = digits[1:]
        if not is_prime(int(''.join((str(d) for d in digits)))):
            return False
        digits = digits[:-1]
        if not is_prime(int(''.join((str(d) for d in digits)))):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True