def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_primes(numbers):
    x = numbers[767]
    primes = [str(p) for p in range(2, x) if is_prime(p)]
    truncatable_primes = []
    for prime_str in primes:
        len_prime_str = len(prime_str)
        is_truncatable = True
        for i in range(len_prime_str):
            if not is_prime(int(prime_str[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(int(prime_str))
    return sorted(truncatable_primes, reverse=True)