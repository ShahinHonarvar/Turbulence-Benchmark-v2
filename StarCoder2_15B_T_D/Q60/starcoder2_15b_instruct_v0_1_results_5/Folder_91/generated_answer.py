def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if int(str_n[i + 1:]) not in primes or int(str_n[:i + 1]) not in primes:
                return False
        return True
    for i in range(11, x + 1):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
    return sorted([p for p in primes if p <= x and is_truncatable_prime(p)], reverse=True)