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

def is_right_truncatable_prime(number):
    if not is_prime(number):
        return False
    while number > 0:
        if not is_prime(number % 10 ** len(str(number))):
            return False
        number //= 10
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[175]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return right_truncatable_primes