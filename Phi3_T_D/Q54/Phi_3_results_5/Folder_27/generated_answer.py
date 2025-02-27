from sympy import isprime

def is_right_truncatable_prime(n):
    if not isprime(n):
        return False
    return all((isprime(int(str(n)[:-i])) for i in range(1, len(str(n)))))

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    return sorted([p for p in range(2, x) if is_right_truncatable_prime(p)], reverse=True)