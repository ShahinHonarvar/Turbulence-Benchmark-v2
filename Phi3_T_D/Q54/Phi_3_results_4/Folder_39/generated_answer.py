def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            remaining = str(i)
            while remaining:
                if not is_prime(int(remaining)):
                    break
                remaining = remaining[:-1]
            else:
                right_truncatable_primes.append(i)
    return right_truncatable_primes