def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 14):
        if num % i == 0:
            multiples.append(i)
    return sum(multiples)