from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[35]

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if isprime(n) and is_left_truncatable(n)], reverse=True)