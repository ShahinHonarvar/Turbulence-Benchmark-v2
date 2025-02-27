def find_sum_of_multiples(integer):
    multiples = []
    for i in range(1, 421):
        if integer % i == 0:
            multiples.append(i)
    return sum(multiples)