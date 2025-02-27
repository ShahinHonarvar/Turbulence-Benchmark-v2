from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[41]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(8, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            primes.append(num)
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)