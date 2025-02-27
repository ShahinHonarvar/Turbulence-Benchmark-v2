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

def is_left_right_truncatable(n, check):
    while n > 0:
        if not is_prime(n):
            return False
        if n < 10 and (not check[n - 1]):
            return False
        n = int(str(n)[1:]) if n > 10 else 0
        if n == 0:
            return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n, {i: is_prime(i) for i in range(x + 1)}):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)