def find_sum_of_multiples(num):
    multiples = range(1, 46)
    sum_of_multiples = sum((num * multiple for multiple in multiples))
    return sum_of_multiples