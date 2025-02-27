import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not sympy.isprime(int(str(n)[i:])) or not sympy.isprime(int(str(n)[:-i])):
                return False
        return sympy.isprime(n)
    x = numbers[77]
    primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)