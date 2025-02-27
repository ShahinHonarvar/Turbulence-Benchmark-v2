def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[645]

    def is_truncatable_prime(n):
        if n < 10:
            return False
        if n < 100:
            return n in (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
        s = str(n)
        return all((int(s[i:]) in prime_cache for i in range(len(s)))) and all((int(s[:i]) in prime_cache for i in range(1, len(s))))
    prime_cache = set((x for x in range(2, x + 1) if is_truncatable_prime(x)))
    return sorted(prime_cache)