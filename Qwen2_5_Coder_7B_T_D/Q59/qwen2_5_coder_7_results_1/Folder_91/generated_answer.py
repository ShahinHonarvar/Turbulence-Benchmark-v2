def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[0]
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)