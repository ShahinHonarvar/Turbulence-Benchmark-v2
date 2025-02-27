def all_left_truncatable_prime(numbers):
    x = numbers[630]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

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

    def is_left_truncatable(n, primes):
        while n > 0:
            if n not in primes:
                return False
            n //= 10
        return True
    for num in range(11, x):
        if is_prime(num) and is_left_truncatable(num, primes):
            left_truncatable_primes.append(num)
            primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)