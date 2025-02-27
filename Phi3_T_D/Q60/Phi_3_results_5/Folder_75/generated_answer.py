def all_left_right_truncatable_prime(numbers):
    x = numbers[40]
    not_prime = set((composites.get(i) for i in range(x + 1)))

    def is_prime(n):
        if n <= 1:
            return False
        if n in not_prime:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                not_prime.update(range(i * 2, n, i))
                return False
            i += 1
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
                return False
        return True
    return sorted((n for n in range(2, x + 1) if is_truncatable(n)))