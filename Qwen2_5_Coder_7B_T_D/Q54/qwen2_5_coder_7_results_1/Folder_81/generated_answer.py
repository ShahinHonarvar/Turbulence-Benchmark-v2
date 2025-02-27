from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    right_truncatable_primes = []

    def is_right_truncatable(p):
        str_p = str(p)
        while str_p:
            if not isprime(int(str_p)):
                return False
            str_p = str_p[:-1]
        return True
    for num in range(2, x):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)