from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[89]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                left_truncatable = False
                break
        if left_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)