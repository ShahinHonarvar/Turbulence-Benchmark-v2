def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        str_n = str_n[:len(str_n) - 1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([p for p in primes if is_right_truncatable_prime(p, primes)], reverse=True)