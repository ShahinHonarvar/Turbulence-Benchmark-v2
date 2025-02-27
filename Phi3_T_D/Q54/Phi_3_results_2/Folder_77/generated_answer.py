def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    return all((is_prime(int(str_n[:-i])) for i in range(1, len(str_n))))

def all_right_truncatable_prime(numbers):
    x = numbers[767]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)