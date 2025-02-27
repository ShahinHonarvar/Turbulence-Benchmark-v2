from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not isprime(num):
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                is_truncatable = False
                break
            if not isprime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)