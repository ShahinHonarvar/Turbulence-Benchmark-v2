from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[67]

    def is_left_truncatable(n):
        n = str(n)
        while n:
            if not isprime(int(n)):
                return False
            n = n[1:]
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable(i)], reverse=True)