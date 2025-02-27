from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[50]
    primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num)):
                if not isprime(int(str_num[:len(str_num) - i])) or not isprime(int(str_num[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)