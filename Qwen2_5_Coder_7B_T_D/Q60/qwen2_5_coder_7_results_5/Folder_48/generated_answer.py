from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[:i + 1] or '0' in str_n[i:]:
                return False
            if not isprime(int(str_n[:i + 1])) or not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes