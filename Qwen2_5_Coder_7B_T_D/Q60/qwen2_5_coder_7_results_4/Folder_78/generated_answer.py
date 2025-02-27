from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[i:]:
                return False
            if not isprime(int(str_n[i:])):
                return False
            if not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])