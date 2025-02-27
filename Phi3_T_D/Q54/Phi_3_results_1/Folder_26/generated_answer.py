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
    x = numbers[81]
    truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1 and is_prime(int(s)):
                s = s[:-1]
            if len(s) == 1:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)