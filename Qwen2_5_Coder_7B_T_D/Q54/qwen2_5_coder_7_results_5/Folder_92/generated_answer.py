from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[7]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        while isprime(num) and num_str:
            num_str = num_str[:-1]
        if not num_str:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)