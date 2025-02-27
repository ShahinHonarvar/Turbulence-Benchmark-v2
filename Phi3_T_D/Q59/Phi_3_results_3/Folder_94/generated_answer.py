from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[43]

    def is_left_truncatable(n):
        if not isprime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    return sorted((x for x in range(2, x) if is_left_truncatable(x)))