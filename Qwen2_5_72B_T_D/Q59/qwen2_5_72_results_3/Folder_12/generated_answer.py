from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for num in range(2, x):
        is_truncatable = True
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)