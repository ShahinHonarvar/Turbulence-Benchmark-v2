def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    primes = []
    for n in range(2, x):
        if is_prime(n):
            n_str = str(n)
            if all((is_prime(int(n_str[i:])) for i in range(len(n_str)))):
                primes.append(n)
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    return left_truncatable_primes(x)