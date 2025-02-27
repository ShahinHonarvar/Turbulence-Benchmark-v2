def all_left_truncatable_prime(numbers):
    x = numbers[466]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if str(n).startswith('0') or not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if str(num).startswith('0') or not is_prime(num):
            continue
        if is_left_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)