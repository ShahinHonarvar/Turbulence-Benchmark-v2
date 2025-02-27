from sympy import isprime

def composite_nums_between_indices(lst):

    def get_composite_numbers(start_index, end_index, numbers):
        return set((number for number in numbers[start_index:end_index + 1] if not isprime(number)))
    return get_composite_numbers(5, 5, lst)