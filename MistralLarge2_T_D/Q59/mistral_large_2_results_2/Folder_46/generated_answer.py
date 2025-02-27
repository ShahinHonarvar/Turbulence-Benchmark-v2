def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)) or '0' in s:
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    primes = []
    num = 2
    while num < x:
        if is_left_truncatable_prime(num):
            primes.append(num)
        num += 1
    return sorted(primes)