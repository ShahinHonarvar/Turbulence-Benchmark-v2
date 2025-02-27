def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncatable_primes(n):
    primes = [2, 3, 5, 7]
    primes_str = list(map(str, primes))
    right_truncatable = []
    while primes[-1] < n:
        for prime_str in primes_str:
            new_prime = int(prime_str[-1] + '0' * (len(str(n)) - len(prime_str)))
            if new_prime < n:
                if is_prime(new_prime):
                    right_truncatable.append(new_prime)
        primes.append(11)
        primes_str.append('11')
    return sorted([x for x in range(2, n) if x in right_truncatable])

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    return truncatable_primes(x)