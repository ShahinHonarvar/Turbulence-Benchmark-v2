from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        while len(str_n) > 1:
            if '0' in str_n or not isprime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return True
    return sorted([n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable_prime(n)], reverse=True)