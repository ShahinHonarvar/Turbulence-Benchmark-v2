import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and sympy.isprime(num):
            is_left_truncatable = True
            for i in range(len(str(num))):
                if not sympy.isprime(int(str(num)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)