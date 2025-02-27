from sympy import isprime

def all_left_truncatable_prime(tuples):
    x = tuples[4]

    def is_left_truncatable(num):
        while num > 0:
            if not isprime(num):
                return False
            num = num % 10 ** (len(str(num)) - 1)
        return True
    return sorted((num for num in range(2, x) if is_left_truncatable(num)))