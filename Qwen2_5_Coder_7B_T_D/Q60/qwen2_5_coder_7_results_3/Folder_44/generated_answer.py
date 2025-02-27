from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
            if not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True
    left_right_truncatable_primes = [n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable(n)]
    return sorted(left_right_truncatable_primes)