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
    x = numbers[52]
    right_truncatable_primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if is_prime(i):
            while s:
                if not is_prime(int(s)):
                    break
                s = s[:-1]
            else:
                right_truncatable_primes.append(i)
    return right_truncatable_primes