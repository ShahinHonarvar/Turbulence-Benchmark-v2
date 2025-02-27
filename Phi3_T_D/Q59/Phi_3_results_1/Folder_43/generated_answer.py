def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        return all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def is_left_truncatable(prime):
        while prime > 0:
            if not is_prime(prime):
                return False
            prime = int(str(prime)[1:])
        return True
    x = numbers[89]
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i)]
    left_truncatables = [p for p in primes if is_left_truncatable(p)]
    return left_truncatables[::-1]