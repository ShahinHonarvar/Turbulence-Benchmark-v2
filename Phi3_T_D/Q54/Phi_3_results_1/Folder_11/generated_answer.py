def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        if n in primes_set:
            str_n = str(n)
            for i in range(1, len(str_n)):
                if int(str_n[i:]) not in primes_set:
                    return False
        else:
            return False
        return True

    def generate_primes(limit):
        primes = []
        for num in range(2, limit + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    x = numbers[86]
    primes = generate_primes(x)
    truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, set(primes))]
    return sorted(truncatable_primes)