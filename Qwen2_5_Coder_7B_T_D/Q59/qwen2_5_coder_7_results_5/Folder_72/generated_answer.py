from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[31]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)