import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]

    def is_truncatable_prime(n):
        if not sympy.isprime(n):
            return False
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str) - 1):
            if not sympy.isprime(int(n_str[i:-i or None])):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes)