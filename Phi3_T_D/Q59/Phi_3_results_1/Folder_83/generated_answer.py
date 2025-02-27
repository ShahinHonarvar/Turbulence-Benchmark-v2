def all_left_truncatable_prime(numbers):
    x = numbers[24]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) for i in range(len(str_n))))
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])