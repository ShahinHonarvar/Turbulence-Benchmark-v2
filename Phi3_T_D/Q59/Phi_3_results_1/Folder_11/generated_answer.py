def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(prime, primes_set):
        while prime > 0:
            if not is_prime(prime):
                return False
            if prime not in primes_set:
                return False
            prime = int(str(prime)[1:])
        return True
    primes = [2, 3, 5, 7]
    for i in range(11, numbers[86]):
        if is_prime(i):
            primes.append(i)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime, set(primes)):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes