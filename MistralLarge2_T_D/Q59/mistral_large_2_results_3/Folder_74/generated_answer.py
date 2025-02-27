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

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    num_str = str(n)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)