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

def all_left_right_truncatable_prime(numbers, k=32):
    x = numbers[k]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        l_truncatable = all((is_prime(int(str_prime[:i])) for i in range(1, len(str_prime))))
        r_truncatable = all((is_prime(int(str_prime[-i:])) for i in range(1, len(str_prime))))
        if l_truncatable and r_truncatable:
            truncatable_primes.append(prime)
    return truncatable_primes