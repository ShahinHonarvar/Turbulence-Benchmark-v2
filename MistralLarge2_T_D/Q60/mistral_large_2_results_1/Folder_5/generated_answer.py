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

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    left, right = (str(n), str(n))
    while len(left) > 1 and len(right) > 1:
        left = left[1:]
        right = right[:-1]
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
        if '0' in left or '0' in right:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)