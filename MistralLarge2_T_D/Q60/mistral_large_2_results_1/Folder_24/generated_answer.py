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
    str_n = str(n)
    for i in range(len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:len(str_n) - i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[65]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)