def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[:len(s) - i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes)