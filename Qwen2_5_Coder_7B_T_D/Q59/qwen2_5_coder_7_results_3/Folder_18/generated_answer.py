from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not isprime(num):
            continue
        all_trunc = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                all_trunc = False
                break
        if all_trunc:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)