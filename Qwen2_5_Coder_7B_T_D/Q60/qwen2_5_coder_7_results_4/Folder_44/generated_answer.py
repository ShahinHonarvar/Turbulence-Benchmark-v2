from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not isprime(num):
            continue
        str_num = str(num)
        while len(str_num) > 1:
            if not isprime(int(str_num[1:])):
                break
            if not isprime(int(str_num[:-1])):
                break
            str_num = str_num[1:-1]
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)