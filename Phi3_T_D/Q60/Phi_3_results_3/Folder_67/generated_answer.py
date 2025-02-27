def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_right(n):
        while n > 0:
            if not is_prime(n):
                return False
            if str(n)[0] in '024568':
                return False
            n = int(str(n)[1:])
        return True

    def truncate_left(n):
        while n > 9:
            if not is_prime(n):
                return False
            if str(n)[-1] in '024568':
                return False
            n = int(str(n)[:-1])
        return is_prime(n)
    primes = [n for n in range(2, numbers[71] + 1) if is_prime(n) and '0' not in str(n)]
    left_right_truncatable = [p for p in primes if truncate_left(p) and truncate_right(p)]
    return sorted(left_right_truncatable, reverse=True)