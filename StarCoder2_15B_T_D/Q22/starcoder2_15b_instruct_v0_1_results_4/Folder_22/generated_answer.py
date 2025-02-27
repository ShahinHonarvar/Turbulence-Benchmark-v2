def find_sum_of_multiples(num):
    multiples = [i for i in range(1, 48) if num * i > 0]
    return sum(multiples)