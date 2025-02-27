def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if not all((is_prime(int(num_str[:i])) for i in range(1, len(num_str) + 1))):
            continue
        primes.append(num)
    return sorted(primes)