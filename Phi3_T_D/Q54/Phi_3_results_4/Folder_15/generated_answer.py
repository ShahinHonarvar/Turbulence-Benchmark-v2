def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        return all((is_prime(int(str(n)[:i])) and is_prime(n) for i in range(len(str(n)), 0, -1)))
    x = num_tuple[6]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)