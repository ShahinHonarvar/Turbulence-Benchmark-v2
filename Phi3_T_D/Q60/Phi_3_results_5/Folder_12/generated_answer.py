def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    s = str(n)
    d = len(s)
    while d > 1 and is_prime(int(s)):
        s = s[1:-1]
        d -= 2
    return is_prime(n) and (not s)

def all_left_right_truncatable_prime(numbers):
    if len(numbers) == 0 or numbers[70] < 11:
        return []
    primes = [i for i in range(11, numbers[70] + 1) if is_prime(i)]
    return [p for p in reversed(primes) if is_truncatable_prime(p, primes)]