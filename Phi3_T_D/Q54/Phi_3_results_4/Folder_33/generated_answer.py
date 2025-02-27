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

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    right_truncatable_primes = []
    for num in range(x - 1, 7, -1):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return right_truncatable_primes