from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    left_right_truncatable_primes = []
    for num in range(1, x + 1):
        if '0' in str(num):
            continue
        if not isprime(num):
            continue
        str_num = str(num)
        if all((isprime(int(str_num[:i])) and isprime(int(str_num[i + 1:])) for i in range(len(str_num) - 1))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)