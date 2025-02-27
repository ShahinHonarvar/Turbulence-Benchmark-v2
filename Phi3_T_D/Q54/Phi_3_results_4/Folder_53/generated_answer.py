def all_right_truncatable_prime(numbers):
    x = numbers[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if n == 0:
            return False
        if n == 0 or not any((n % p == 0 for p in primes)):
            return True
        return is_right_truncatable_prime(n // 10, primes)

    def find_right_truncatable_primes(n):
        primes = [2]
        right_truncatable_primes = []
        for num in range(2, n):
            if is_right_truncatable_prime(num, primes):
                right_truncatable_primes.append(num)
            if is_prime(num):
                primes.append(num)
        return right_truncatable_primes
    return sorted(find_right_truncatable_primes(x), reverse=True)