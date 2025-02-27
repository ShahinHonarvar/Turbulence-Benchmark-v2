from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[33]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            while str_num and isprime(int(str_num)):
                str_num = str_num[:-1]
            if not str_num:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)