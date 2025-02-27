def all_left_truncatable_prime(numbers):
    x = numbers[433]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for i in range(len(str(n))):
            if int(str(n)[i:]) not in primes_set:
                return False
        return True
    primes = []
    primes_set = set()
    n = 2
    while True:
        if is_prime(n):
            primes.append(n)
            primes_set.add(n)
            if n >= x:
                break
        n += 1
    left_truncatable_primes = [p for p in primes if is_left_truncatable(p)]
    return sorted(left_truncatable_primes, reverse=True)