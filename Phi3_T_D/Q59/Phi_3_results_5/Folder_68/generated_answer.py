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

def all_left_truncatable_prime(t):
    x = t[1]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            for j in range(len(s)):
                if not is_prime(int(s[j:])):
                    break
            else:
                left_truncatable_primes.append(i)
    return left_truncatable_primes