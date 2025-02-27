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
    x = numbers[93]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            if not is_prime(int(str(i)[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)