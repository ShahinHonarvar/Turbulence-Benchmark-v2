def all_right_truncatable_prime(numbers):
    x = numbers[125]
    right_truncatables = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if n < 10 or not is_prime(n):
            return False
        return all((number % 10 == m and is_right_truncatable_prime(number // 10, primes) for m in range(3, 7, 2)))
    primes = set()
    for i in range(2, x):
        if is_right_truncatable_prime(i, primes):
            primes.add(i)
    return sorted(list(primes), reverse=True)