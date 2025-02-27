from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    return [p for p in (num for num in range(2, x) if isprime(num)) if all((isprime(int(str(p)[i:])) for i in range(len(str(p)))))]