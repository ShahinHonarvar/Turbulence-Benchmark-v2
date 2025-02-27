def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, from_right=True):
    if from_right:
        last_digit = n % 10
        if last_digit in (0, 2, 4, 5, 6, 8):
            return False
    result = [n]
    while n > 0:
        n //= 10
        if n == 0:
            break
        if from_right:
            if not is_prime(n):
                return False
        elif not is_prime(n) or n % 10 in (0, 2, 4, 5, 6, 8):
            return False
        result.append(n)
    return result[::-1] if from_right else result

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[767]
    truncatable_primes = []
    for n in range(7, x):
        if is_prime(n) and is_truncatable_prime(n, from_right=False):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)