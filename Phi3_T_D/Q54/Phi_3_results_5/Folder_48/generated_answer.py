def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n, first_digit):
        if n < 10 and n != first_digit:
            return False
        return is_prime(n) and all((is_right_truncatable_prime(int(str(n)[:-1]), first_digit) if n != str(first_digit) else True for _ in range(2, len(str(n)) + 1)))
    x = input_tuple[835]
    right_truncatable_primes = []
    first_digit = 2
    while first_digit < x:
        for n in range(first_digit, x, first_digit):
            if is_right_truncatable_prime(n, first_digit):
                right_truncatable_primes.append(n)
        first_digit = int(str(first_digit)[0]) + 1
    return sorted(right_truncatable_primes)