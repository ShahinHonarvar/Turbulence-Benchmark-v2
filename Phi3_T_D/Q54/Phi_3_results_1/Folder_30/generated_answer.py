def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    if n < 10 or not is_prime(n):
        return False
    return all((is_prime(int(str(n)[:-i])) for i in range(1, len(str(n)))))

def all_right_truncatable_prime(numbers):
    x = numbers[37]
    right_truncatables = []
    for i in range(10, x, 2):
        if is_right_truncatable_prime(i, right_truncatables):
            right_truncatables.append(i)
    return sorted(right_truncatables, reverse=True)