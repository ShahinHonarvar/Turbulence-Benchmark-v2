def all_left_truncatable_prime(numbers):
    x = numbers[100]
    left_truncatable_primes = []
    for prime in primes_less_than(x):
        if '0' not in str(prime):
            left_truncatable = True
            for i in range(1, len(str(prime))):
                truncated_prime = int(str(prime)[i:])
                if truncated_prime not in primes_less_than(x):
                    left_truncatable = False
                    break
            if left_truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)

def primes_less_than(x):
    return [prime for prime in range(2, x) if is_prime(prime)]

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True