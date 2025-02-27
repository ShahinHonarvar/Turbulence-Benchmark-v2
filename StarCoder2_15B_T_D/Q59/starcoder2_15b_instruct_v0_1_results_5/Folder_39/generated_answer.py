def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = []
    for i in range(2, x):
        if not is_prime(i):
            continue
        j = i
        while j < x:
            if not is_prime(j):
                break
            j //= 10
        else:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)