def all_right_truncatable_prime(numbers):
    limit = numbers[31]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    prime_candidates = set([2, 3, 5, 7])
    truncatable_primes = []
    for prime in prime_candidates:
        temp = prime
        while temp < limit:
            temp *= 10
            truncatable_primes.append(temp)
    return sorted([num for num in truncatable_primes if num < limit and is_right_truncatable(num)], reverse=True)