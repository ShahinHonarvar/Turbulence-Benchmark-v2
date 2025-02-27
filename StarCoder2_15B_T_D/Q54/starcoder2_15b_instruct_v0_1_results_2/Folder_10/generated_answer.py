def all_right_truncatable_prime(tup):

    def is_right_truncatable_prime(num):
        while num > 0:
            if num < 2 or (num != 2 and num % 2 == 0):
                return False
            if num < 3 or (num != 3 and num % 3 == 0):
                return False
            if num < 5 or (num != 5 and num % 5 == 0):
                return False
            if num < 7 or (num != 7 and num % 7 == 0):
                return False
            num //= 10
        return True
    x = tup[38]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)