def all_left_truncatable_prime(numbers):
    x = numbers[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))
    primes = [n for n in range(2, x) if is_prime(n) and '0' not in str(n)]
    return sorted(filter(is_left_truncatable, primes))