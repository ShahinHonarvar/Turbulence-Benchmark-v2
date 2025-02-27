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

def all_left_truncatable_prime(numbers):
    x = numbers[90]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            left_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(i)
    return primes