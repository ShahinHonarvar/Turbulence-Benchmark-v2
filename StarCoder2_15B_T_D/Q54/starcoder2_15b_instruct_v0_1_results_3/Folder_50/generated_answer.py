def all_right_truncatable_prime(tup):
    x = tup[57]
    primes = [num for num in range(2, x) if is_prime(num)]
    right_truncatable_primes = []
    for prime in primes:
        truncated_prime = prime
        while truncated_prime >= 10:
            truncated_prime //= 10
            if not is_prime(truncated_prime):
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True