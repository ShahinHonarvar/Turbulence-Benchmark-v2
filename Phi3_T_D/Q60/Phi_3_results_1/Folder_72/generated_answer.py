def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) != 32:
        raise ValueError('Expected a tuple of 32 integers.')
    x = numbers[31]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return [p for p in primes if is_left_right_truncatable(p, primes)]