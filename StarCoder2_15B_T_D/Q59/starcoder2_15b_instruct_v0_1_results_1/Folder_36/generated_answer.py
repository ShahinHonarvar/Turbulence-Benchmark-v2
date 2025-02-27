def all_left_truncatable_prime(tup):
    x = tup[992]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)))