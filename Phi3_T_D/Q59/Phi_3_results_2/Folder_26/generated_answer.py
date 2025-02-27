from sympy import isprime

def all_left_truncatable_prime(numbers):
    thresh, = numbers[81]

    def is_left_truncatable_prime(n, prime_set):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    left_truncatable_primes = [n for n in range(2, thresh) if is_left_truncatable_prime(n, set(map(isprime, range(2, thresh))))]
    return sorted(left_truncatable_primes, reverse=True)