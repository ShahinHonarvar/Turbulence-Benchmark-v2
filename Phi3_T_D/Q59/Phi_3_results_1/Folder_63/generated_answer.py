def all_left_truncatable_prime(numbers, index=88):
    x = numbers[index]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    all_primes = [p for p in range(2, x) if is_prime(p)]
    return sorted([p for p in all_primes if is_left_truncatable(p, all_primes)])