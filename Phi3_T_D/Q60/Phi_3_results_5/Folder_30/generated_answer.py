def all_left_right_truncatable_prime(tuples):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i or None])) for i in range(len(str_n))))
    x = tuples[37] if len(tuples) > 37 else 0
    if x < 11:
        return []
    primes = []
    for number in range(x, 1, -1):
        if str(number).startswith('0') or not is_prime(number):
            continue
        if truncatable(number):
            primes.append(number)
    return primes