def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_primes(numbers):
    x = numbers[6]
    truncatable_primes = []
    for p in range(x, 1, -1):
        if is_prime(p):
            if all((is_prime(int(str(p)[:i] + str(p)[i + 1:])) for i in range(len(str(p))))):
                truncatable_primes.append(p)
    return truncatable_primes