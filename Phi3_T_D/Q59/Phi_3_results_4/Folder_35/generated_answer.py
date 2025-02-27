from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[177]

    def is_left_truncatable(n):
        if not isprime(n):
            return False
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)])