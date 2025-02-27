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

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    right_truncatable_primes = []
    for prime in range(2, x):
        num_str = str(prime)
        is_truncatable = True
        for i in range(len(num_str) - 1, -1, -1):
            if not is_prime(int(num_str[:i + 1])):
                is_truncatable = False
                break
        if is_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)