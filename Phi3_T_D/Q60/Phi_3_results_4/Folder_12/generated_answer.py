def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            l_trunc = int(str_n[i:])
            r_trunc = int(str_n[:-i]) if i > 0 else 0
            if not is_prime(l_trunc) or not is_prime(r_trunc):
                return False
        return True
    x = numbers[70]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)