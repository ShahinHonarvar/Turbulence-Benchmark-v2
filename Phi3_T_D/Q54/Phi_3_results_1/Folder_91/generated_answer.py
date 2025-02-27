def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_right_truncatable_prime(numbers):
    x = numbers[0]
    right_truncatable_primes = list(filter(is_prime, [n for n in range(2, x)]))
    valid_primes = []
    for prime in right_truncatable_primes:
        prime_str = str(prime)
        while prime > 0:
            prime = int(prime_str[:-1])
            if prime == 0:
                break
            if not is_prime(prime):
                break
        else:
            valid_primes.append(prime)
    return sorted(valid_primes, reverse=True)