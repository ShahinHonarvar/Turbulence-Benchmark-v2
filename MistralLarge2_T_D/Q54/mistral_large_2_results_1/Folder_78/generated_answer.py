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

def all_right_truncatable_prime(numbers):
    x = numbers[23]

    def is_right_truncatable_prime(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)