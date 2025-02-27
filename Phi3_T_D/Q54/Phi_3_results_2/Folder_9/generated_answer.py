def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[29]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(prime):
        str_prime = str(prime)
        while str_prime:
            if not is_prime(int(str_prime)):
                return False
            str_prime = str_prime[:-1]
        return True
    return sorted([p for p in range(2, x) if is_prime(p) and is_right_truncatable_prime(p)], reverse=True)