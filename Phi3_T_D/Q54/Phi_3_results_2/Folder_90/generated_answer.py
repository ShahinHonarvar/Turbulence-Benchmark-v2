from sympy import isprime

def all_right_truncatable_prime(values):
    x = values[466]
    if x < 11:
        return []
    right_truncatable_primes = ['2', '3', '5', '7']
    for p in range(11, x, 2):
        p_str = str(p)
        for i in range(len(p_str)):
            if not isprime(int(p_str[i:])):
                break
        else:
            right_truncatable_primes.append(str(p))
    right_truncatable_primes = sorted(right_truncatable_primes, key=lambda x: int(x), reverse=True)
    return right_truncatable_primes