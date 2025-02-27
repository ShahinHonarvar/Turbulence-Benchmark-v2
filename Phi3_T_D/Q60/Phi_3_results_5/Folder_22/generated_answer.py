def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[85]
    prime_list = [p for p in range(2, x + 1) if is_prime(p)]
    trunc_primes = [p for p in prime_list if is_truncatable_prime(p, prime_list)]
    return trunc_primes