from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num) or not isprime(num):
            continue
        is_left_truncatable = True
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)