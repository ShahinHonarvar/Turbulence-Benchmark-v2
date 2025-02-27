from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)