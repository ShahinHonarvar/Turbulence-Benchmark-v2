from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            str_num = str(num)
            while str_num:
                if not isprime(int(str_num)):
                    break
                str_num = str_num[1:]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)