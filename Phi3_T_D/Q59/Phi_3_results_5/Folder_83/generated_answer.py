from sympy import primerange, isprime

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    primes = list(primerange(2, x))
    left_truncatable = []
    for p in primes:
        p_str = str(p)
        is_left_truncatable = True
        for i in range(len(p_str)):
            if not isprime(int(p_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            yield p