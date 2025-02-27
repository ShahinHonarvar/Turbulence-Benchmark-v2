def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def left_right_truncatable(n, primes):
    if n in primes:
        left = n // 10
        right = n % 10
        return is_prime(left) and is_prime(right)
    return False

def all_left_right_truncatable_prime(numbers):
    if numbers[4] < 11:
        return []
    x = numbers[4]
    primes = {2, 3, 5, 7}
    for i in range(11, x + 1):
        if is_prime(i):
            primes.add(i)
    result = {}
    for prime in primes:
        if left_right_truncatable(prime, primes):
            result[prime] = True
    return sorted(result.keys())