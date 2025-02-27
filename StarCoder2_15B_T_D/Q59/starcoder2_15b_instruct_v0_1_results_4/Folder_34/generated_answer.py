def all_left_truncatable_prime(tup):
    x = tup[18]
    single_digit_primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def generate_left_truncatable_primes(num, primes):
        if num < x:
            left_truncatable_primes.append(num)
            for prime in single_digit_primes:
                if num * 10 + prime in primes:
                    generate_left_truncatable_primes(num * 10 + prime, primes)
    for prime in single_digit_primes:
        generate_left_truncatable_primes(prime, left_truncatable_primes)
    return sorted(left_truncatable_primes, reverse=True)