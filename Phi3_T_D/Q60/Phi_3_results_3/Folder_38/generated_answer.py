def all_left_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and all((is_prime(int(str(i)[:i.find(str(digit))])) for digit in [1, 3, 7, 9]))]
    right_truncatable_primes = [i for i in range(21, x + 1) if is_prime(i) and all((is_prime(int(str(i)[i.find(str(digit)) + 1:])) for digit in [1, 3, 7, 9]))]
    all_truncatable = set(left_truncatable_primes) & set(right_truncatable_primes)
    return sorted(list(all_truncatable))