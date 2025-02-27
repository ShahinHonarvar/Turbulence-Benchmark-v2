def all_left_right_truncatable_prime(values):
    primes = [2, 3, 5, 7]
    x = values[93]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))
    return [p for p in primes if p <= x] + [p for p in range(max(primes) + 1, x + 1) if is_prime(p) and is_truncatable(p)]