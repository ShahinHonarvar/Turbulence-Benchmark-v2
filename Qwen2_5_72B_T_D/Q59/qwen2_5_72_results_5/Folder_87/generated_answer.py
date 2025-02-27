from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)