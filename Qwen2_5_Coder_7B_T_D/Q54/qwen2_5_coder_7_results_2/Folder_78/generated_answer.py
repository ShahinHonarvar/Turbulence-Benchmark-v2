def all_right_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            if is_right_truncatable_prime(num):
                primes.append(num)
    return sorted(primes)

def is_right_truncatable_prime(num):
    while num > 0:
        if num % 2 == 0 or num % 3 == 0:
            return False
        num //= 10
    return True