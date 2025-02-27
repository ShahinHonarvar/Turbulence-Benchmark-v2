from sympy import isprime, primerange

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    primes = set(primerange(2, x))
    right_truncatable_primes = []
    while primes:
        prime = primes.pop()
        s = str(prime)
        for i in range(len(s), 0, -1):
            truncated = int(s[:i])
            if truncated not in primes:
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)