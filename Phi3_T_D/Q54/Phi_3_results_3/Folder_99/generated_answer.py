def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(integers):
    x = integers[758]
    right_truncatable_primes = []

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for prime in integers:
        if prime >= 10 and is_prime(prime) and is_right_truncatable(prime):
            right_truncatable_primes.append(prime)
    return sorted(list(set(right_truncatable_primes)))[:x]