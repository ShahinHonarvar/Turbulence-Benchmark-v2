def all_left_truncatable_prime(numbers):
    x = numbers[92]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2 or any((n % p == 0 for p in range(2, int(n ** 0.5) + 1))):
            return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n in primes:
                n //= 10
            else:
                return False
        return True
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)