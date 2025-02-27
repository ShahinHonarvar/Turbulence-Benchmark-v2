from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[835]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_left_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)