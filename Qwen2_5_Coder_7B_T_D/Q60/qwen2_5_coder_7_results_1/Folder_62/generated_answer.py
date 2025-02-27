from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[i:] or not isprime(int(str_n[i:])):
                return False
            if '0' in str_n[:i + 1] or not isprime(int(str_n[:i + 1])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)])