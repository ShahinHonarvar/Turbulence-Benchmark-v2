def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        return all((is_left_right_prime(int(str_n[i:])) and is_left_right_prime(int(str_n[:-i or None])) for i in range(1, len(str_n))))

    def all_left_right_prime(prime_list, current):
        if not any((str(p).startswith(current) and str(p).endswith(current) for p in prime_list)):
            return prime_list
        next_primes = {p for p in primes if str(p).startswith(current) and str(p).endswith(current)}
        return all_left_right_prime(prime_list.union(next_primes), str(int(current) + 1).zfill(len(current)))
    primes = set(filter(is_prime, range(2, numbers[93] + 1)))
    return sorted((p for p in all_left_right_prime(set(), '1') if p <= numbers[93]))