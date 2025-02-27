from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(p):
        str_p = str(p)
        for i in range(len(str_p)):
            if not isprime(int(str_p[i:])):
                return False
            if not isprime(int(str_p[:len(str_p) - i])):
                return False
        return True
    x = numbers[86]
    truncatable_primes = [p for p in range(2, x + 1) if isprime(p) and '0' not in str(p) and is_left_right_truncatable(p)]
    return sorted(truncatable_primes)