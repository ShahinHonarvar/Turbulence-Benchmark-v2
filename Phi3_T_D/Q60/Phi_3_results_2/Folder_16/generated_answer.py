def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_all_digits_prime(n):
    while n > 0:
        if not is_prime(n % 10):
            return False
        n //= 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    truncatable_primes = [str(p) for p in range(23, x) if is_all_digits_prime(p)]
    left_right_truncatable_primes = []
    for prime in truncatable_primes:
        for i in range(1, len(prime)):
            if not is_prime(int(prime[i:])) or not is_prime(int(prime[:i])):
                break
        else:
            left_right_truncatable_primes.append(int(prime))
    return sorted(left_right_truncatable_primes)