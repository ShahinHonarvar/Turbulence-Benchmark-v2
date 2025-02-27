from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    left_right_truncatable_primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)