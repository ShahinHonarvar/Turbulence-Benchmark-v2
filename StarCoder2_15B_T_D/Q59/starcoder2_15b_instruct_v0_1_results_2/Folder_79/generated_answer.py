def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    left_truncatable_primes = []
    for i in range(2, x):
        number = i
        is_left_truncatable = True
        while number >= 10:
            if not is_prime(number):
                is_left_truncatable = False
                break
            number //= 10
        if is_left_truncatable and is_prime(number):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)