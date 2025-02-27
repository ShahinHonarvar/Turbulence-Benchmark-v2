def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes_set):
    if '0' in str(n):
        return False
    if n not in primes_set:
        return False
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))

def all_left_right_truncatable_primes(numbers):
    x = numbers[84]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [prime for prime in primes if is_truncatable_prime(prime, set(primes))]
    return sorted(truncatable_primes, reverse=True)