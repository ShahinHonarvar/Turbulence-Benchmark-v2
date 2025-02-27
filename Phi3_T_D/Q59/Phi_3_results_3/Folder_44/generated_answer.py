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

def all_left_truncatable_primes(numbers):
    x = numbers[39]
    truncatable_primes = []

    def is_left_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    for n in range(23, x):
        if is_left_truncatable(n):
            truncatable_primes.append(n)
    return truncatable_primes