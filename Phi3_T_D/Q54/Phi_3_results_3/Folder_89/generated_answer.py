def all_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        return is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1) if int(str(n)[:i]) > 1))
    primes_set = {2, 3, 5, 7}
    if len(numbers_tuple) != 1 or numbers_tuple[0] < 10:
        return []
    x = numbers_tuple[0]
    while x > 0:
        if is_right_truncatable_prime(x, primes_set):
            primes_set.add(x)
        x -= 1
    return sorted(primes_set - {2, 3, 5, 7}, reverse=True)