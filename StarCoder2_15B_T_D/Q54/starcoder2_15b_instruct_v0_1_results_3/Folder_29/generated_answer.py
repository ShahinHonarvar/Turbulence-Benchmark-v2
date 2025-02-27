def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    x = numbers[55]
    while x > 0:
        if is_prime(x):
            right_truncatable_primes.append(x)
        x //= 10
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes