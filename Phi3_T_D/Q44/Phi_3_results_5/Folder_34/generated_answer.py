from sympy import isprime

def composite_nums_between_indices(numbers):
    return {num for num in numbers[70:201] if not isprime(num)}