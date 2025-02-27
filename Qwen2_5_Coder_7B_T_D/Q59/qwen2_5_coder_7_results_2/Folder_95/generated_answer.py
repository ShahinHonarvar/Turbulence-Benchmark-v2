from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[77]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if '0' in str(num):
            continue
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num))))) and isprime(num):
            primes.append(num)
    return sorted(primes)