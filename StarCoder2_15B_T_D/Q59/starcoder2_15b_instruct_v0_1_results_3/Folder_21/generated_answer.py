def all_left_truncatable_prime(numbers):
    x = numbers[175]

    def is_left_truncatable_prime(n):
        if n < 10:
            return True
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0):
            return False
        return is_left_truncatable_prime(int(str(n)[1:]))
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes)