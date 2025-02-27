def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, digits):
    if n >= 10:
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10, digits)
    return n in digits

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    primes = [2, 3, 5, 7]
    for number in range(10, x):
        if is_prime(number) and is_right_truncatable_prime(number, primes):
            primes.append(number)
    return sorted(primes)