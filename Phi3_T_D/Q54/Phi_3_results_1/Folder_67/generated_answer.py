def all_right_truncatable_prime(numbers):

    def is_prime(n, sieve):
        if n < 2:
            return False
        for i in sieve:
            if i * i > n:
                break
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, sieve):
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n), sieve):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[71] if 71 < len(numbers) else 0
    sieve = [True] * (x + 1)
    sieve[0], sieve[1] = (False, False)
    primes = [2]
    for i in range(3, x + 1, 2):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, x + 1, i):
                sieve[j] = False
    right_truncatable_primes = [p for p in reversed(primes) if is_right_truncatable_prime(p, primes)]
    return right_truncatable_primes