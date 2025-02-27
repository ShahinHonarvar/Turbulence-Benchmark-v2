from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[31]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes