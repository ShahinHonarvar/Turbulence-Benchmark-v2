def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and all((is_prime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)