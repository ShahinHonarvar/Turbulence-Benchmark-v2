from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[81]
    left_right_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and all((isprime(int(str_num[:i])) and isprime(int(str_num[i + 1:])) for i in range(len(str_num) - 1))):
            left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)