def all_left_right_truncatable_prime(primes_tuple):
    is_prime = set(primes_tuple)

    def is_left_right_truncatable(num):
        if num < 10:
            return num in is_prime
        while num >= 10:
            if num not in is_prime or not is_left_truncatable(int(str(num)[1:])):
                return False
            num = int(str(num)[:-1])
        return num == 2 or num == 3 or num == 5 or (num == 7)

    def is_left_truncatable(num):
        while num >= 10:
            num = int(str(num)[1:])
            if num not in is_prime:
                return False
        return True
    x = primes_tuple[77]
    left_right_truncatable_primes = [p for p in is_prime if is_left_truncatable(p) and is_left_right_truncatable(p) and (p <= x)]
    return sorted(left_right_truncatable_primes, reverse=True)