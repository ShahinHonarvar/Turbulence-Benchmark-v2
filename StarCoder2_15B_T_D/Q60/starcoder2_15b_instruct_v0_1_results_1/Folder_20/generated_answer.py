def all_left_right_truncatable_prime(tuple_of_pos_ints):
    x = tuple_of_pos_ints[100]

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)