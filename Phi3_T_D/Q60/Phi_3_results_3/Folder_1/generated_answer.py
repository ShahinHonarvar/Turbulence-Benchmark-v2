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

def is_left_and_right_truncatable_prime(n, length, check_truncated=True):
    if len(str(n)) < length or (check_truncated and (not is_prime(n))):
        return False
    for i in range(length - 1):
        if not is_prime(int(str(n)[:i + 1])) or not is_prime(int(str(n)[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    primes = []
    for number in range(x, 1, -1):
        if is_prime(number) and is_left_and_right_truncatable_prime(number, len(str(number)), check_truncated=True):
            primes.append(number)
    return primes