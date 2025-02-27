def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    if '0' in n_str:
        return False
    left, right = (n_str, n_str)
    while len(left) > 1 and len(right) > 1:
        left = left[1:]
        right = right[:-1]
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes