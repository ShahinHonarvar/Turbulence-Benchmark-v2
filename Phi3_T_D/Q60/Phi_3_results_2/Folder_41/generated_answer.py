def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 46:
        x = numbers[46]
    else:
        return []
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    result = [p for p in primes if is_truncatable_prime(p, primes)]
    return sorted(result, reverse=True)