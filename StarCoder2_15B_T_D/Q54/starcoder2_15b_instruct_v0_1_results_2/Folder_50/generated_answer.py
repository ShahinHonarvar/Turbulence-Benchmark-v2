def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_rightmost_digit(num):
    return num // 10

def is_right_truncatable_prime(num):
    if is_prime(num):
        if num < 10:
            return True
        return is_right_truncatable_prime(remove_rightmost_digit(num))
    return False

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)