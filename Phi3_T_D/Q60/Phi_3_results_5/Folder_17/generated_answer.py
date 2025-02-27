import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = []

    def is_left_right_truncatable(num):
        str_num = str(num)
        while len(str_num) > 1:
            if not sympy.isprime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        return True
    for prime_candidate in range(2, x + 1):
        if sympy.isprime(prime_candidate) and is_left_right_truncatable(prime_candidate):
            truncatable_primes.append(prime_candidate)
    return sorted(truncatable_primes, reverse=True)