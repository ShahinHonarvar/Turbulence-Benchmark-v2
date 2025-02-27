from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for p in primes:
        str_p = str(p)
        while len(str_p) > 0:
            if not isprime(int(str_p)):
                break
            str_p = str_p[1:]
        else:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)