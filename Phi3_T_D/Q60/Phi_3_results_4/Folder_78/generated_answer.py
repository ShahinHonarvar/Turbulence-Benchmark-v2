def all_left_right_truncatable_prime(range_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
                return False
        return True
    x = range_integers[23 - 1]
    return [i for i in range(2, x + 1) if is_truncatable_prime(i)]