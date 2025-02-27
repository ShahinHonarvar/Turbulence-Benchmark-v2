def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return '0' not in str_n

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    primes = []
    for num in range(2, x):
        if left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)