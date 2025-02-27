def find_sum_of_multiples(num):
    multiples = [i for i in range(1, 30) for j in range(1, num + 1) if i * j == num]
    return sum(multiples)