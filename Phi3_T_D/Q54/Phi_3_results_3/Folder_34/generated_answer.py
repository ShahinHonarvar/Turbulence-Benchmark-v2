def all_right_truncatable_prime(numbers):
    x = numbers[18]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        str_n = str(n)
        return all((is_prime(int(str_n[:-i])) for i in range(1, len(str_n)))) and is_prime(n)
    primes = [2]
    for num in range(3, x, 2):
        if is_prime(num):
            primes.append(num)
            if is_right_truncatable_prime(num, primes):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)