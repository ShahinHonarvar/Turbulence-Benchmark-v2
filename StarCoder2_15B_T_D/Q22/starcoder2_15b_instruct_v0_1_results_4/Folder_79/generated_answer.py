def find_sum_of_multiples(num):
    multiples = [i for i in range(1, 29)]
    sum_of_multiples = sum((num * i for i in multiples))
    return sum_of_multiples