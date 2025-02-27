def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def get_right_truncatable_primes(n):
        primes = [2, 3, 5, 7]
        while primes[-1] < n:
            candidate = primes[-1] + 2
            if is_prime(candidate):
                primes.append(candidate)
        return primes
    topx = numbers[432]
    primes = get_right_truncatable_primes(topx)

    def is_right_truncatable(n, primes_set):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if int(str_n[:i]) not in primes_set:
                return False
        return True
    primes_set = set(primes)
    right_truncatable_primes = [primes[0]]
    for prime in primes[1:]:
        if is_right_truncatable(prime, primes_set):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)