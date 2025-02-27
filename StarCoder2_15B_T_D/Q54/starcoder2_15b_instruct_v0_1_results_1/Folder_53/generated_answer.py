def all_right_truncatable_prime(tup):
    x = tup[86]
    right_truncatable_primes = []

    def is_right_truncatable_prime(num):
        if num < 10 and num in [2, 3, 5, 7]:
            return True
        if num % 10 in [0, 2, 4, 5, 6, 8] or num % 10 == 9:
            return False
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        return is_right_truncatable_prime(num // 10)
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)