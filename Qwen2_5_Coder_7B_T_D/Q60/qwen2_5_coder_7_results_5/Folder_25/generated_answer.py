import sympy

def all_left_right_truncatable_prime(t):
    x = t[92]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and sympy.isprime(num):
            str_num = str(num)
            while len(str_num) > 1 and sympy.isprime(int(str_num)):
                str_num = str_num[1:]
            str_num = str(num)
            while len(str_num) > 1 and sympy.isprime(int(str_num)):
                str_num = str_num[:-1]
            if len(str_num) == 1 or len(str_num) == 2:
                primes.append(num)
    return sorted(list(set(primes)))