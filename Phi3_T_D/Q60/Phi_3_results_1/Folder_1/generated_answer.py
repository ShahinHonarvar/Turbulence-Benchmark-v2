import sympy

def all_left_right_truncatable_prime(range_tuple):

    def is_left_and_right_truncatable_prime(n):
        str_n = str(n)
        len_n = len(str_n)
        for i in range(len_n):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:i + 1])):
                return False
        return True
    upper_limit = range_tuple[20]
    primes = [i for i in range(2, upper_limit + 1) if sympy.isprime(i)]
    left_and_right_truncatable_primes = filter(is_left_and_right_truncatable_prime, primes)
    result = sorted(list(left_and_right_truncatable_primes), reverse=True)
    return result