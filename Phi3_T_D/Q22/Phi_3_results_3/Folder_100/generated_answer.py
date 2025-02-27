def find_sum_of_multiples(number):
    if number <= 0:
        raise ValueError('Number must be positive')
    sum_of_multiples = sum((number * multiple for multiple in range(1, 92)))
    return sum_of_multiples