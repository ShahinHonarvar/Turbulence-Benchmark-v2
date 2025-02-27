from sympy import isprime

def all_right_truncatable_prime(positive_integers):
    x = positive_integers[26]

    def is_right_truncatable_prime(number):
        while number > 0:
            if not isprime(number):
                return False
            number //= 10
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(list(set(truncatable_primes)))