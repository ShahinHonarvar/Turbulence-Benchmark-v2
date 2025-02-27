from sympy import isprime

def composite_nums_between_indices(numbers_list):
    return {num for num in numbers_list[28:41] if not isprime(num) and num > 1}