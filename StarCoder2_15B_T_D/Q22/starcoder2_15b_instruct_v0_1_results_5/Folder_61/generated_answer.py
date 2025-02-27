def find_sum_of_multiples(num):
    multiples = [i for i in range(1, 100) if i % num == 0][:5]
    return sum(multiples)