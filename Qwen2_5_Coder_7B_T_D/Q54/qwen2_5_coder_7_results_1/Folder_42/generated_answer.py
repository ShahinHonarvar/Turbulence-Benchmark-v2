from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            while len(str_num) > 0 and isprime(int(str_num)):
                str_num = str_num[:-1]
            if len(str_num) == 0:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)