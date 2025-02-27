def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        last_digit = n % 10
        if not is_prime(int(str(n)[:-1])):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[19]
    return sorted(filter(is_right_truncatable_prime, range(2, x)))