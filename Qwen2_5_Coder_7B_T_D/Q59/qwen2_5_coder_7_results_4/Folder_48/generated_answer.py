from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[835]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if not isprime(num):
            continue
        str_num = str(num)
        while len(str_num) > 1:
            if not isprime(int(str_num)):
                break
            str_num = str_num[1:]
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)