def find_sum_of_multiples(integer):
    sum_of_multiples = sum((integer * i for i in range(1, 393)))
    return sum_of_multiples