from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            all_trunc = True
            for i in range(len(str_p)):
                if not isprime(int(str_p[i:])):
                    all_trunc = False
                    break
            if all_trunc:
                left_truncatable.append(p)
    return sorted(left_truncatable, reverse=True)