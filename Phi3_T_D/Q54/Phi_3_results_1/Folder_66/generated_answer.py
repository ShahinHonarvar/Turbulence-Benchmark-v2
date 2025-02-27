def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, prime_set):
        while n:
            if not is_prime(n):
                return False
            if n not in prime_set:
                return False
            n = n // 10
        return True
    primes = set()
    for num in range(2, numbers[25]):
        if is_prime(num):
            primes.add(num)
    right_truncatable_primes = [num for num in primes if is_truncatable(num, primes)]
    return sorted(right_truncatable_primes, reverse=True)