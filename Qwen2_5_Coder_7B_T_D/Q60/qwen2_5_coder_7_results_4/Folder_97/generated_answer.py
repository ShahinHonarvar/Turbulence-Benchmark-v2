from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[645]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
            if '0' in str_num[:i + 1]:
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)