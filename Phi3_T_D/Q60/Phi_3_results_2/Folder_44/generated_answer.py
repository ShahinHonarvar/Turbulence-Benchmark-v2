def all_left_right_truncatable_prime(tuple_of_ints):

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

    def is_truncatable(prime):
        str_prime = str(prime)
        return all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:len(str_prime) - i])) for i in range(len(str_prime))))

    def truncatable_primes_within_range(upper_limit):
        potential_primes = filter(is_prime, range(2, upper_limit + 1))
        return filter(is_truncatable, potential_primes)
    x = tuple_of_ints[39]
    return sorted(list(truncatable_primes_within_range(x)))