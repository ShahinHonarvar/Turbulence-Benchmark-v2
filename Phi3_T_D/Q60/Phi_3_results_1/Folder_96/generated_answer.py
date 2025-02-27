def all_left_right_truncatable_prime(numbers):
    primes = {2, 3, 5, 7}
    for i in range(11, numbers[29] + 1, 2):
        if all((i % p != 0 for p in primes)):
            primes.add(i)

    def is_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not int(str_n[i:]) in primes or not int(str_n[:i + 1]) in primes:
                return False
        return True
    return [n for n in primes if n <= numbers[29] and is_truncatable_prime(n, primes)]