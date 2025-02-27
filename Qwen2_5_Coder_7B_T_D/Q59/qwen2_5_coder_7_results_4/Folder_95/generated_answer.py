def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True