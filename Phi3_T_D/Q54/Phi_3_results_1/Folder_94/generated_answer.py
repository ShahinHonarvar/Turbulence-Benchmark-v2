def all_right_truncatable_prime(numbers):
    x = numbers[42]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        primes.append(n)
        return True
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num, right_truncatable_primes):
            pass
    return sorted(right_truncatable_primes)