def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(number):
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    return True

def all_right_truncatable_primes(numbers):
    x = numbers[992]
    trunc_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return trunc_primes