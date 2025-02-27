from sympy import isprime

def is_left_right_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if not isprime(int(str_num[i + 1:])) or not isprime(int(str_num[:-(i + 1)])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num) and is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes)