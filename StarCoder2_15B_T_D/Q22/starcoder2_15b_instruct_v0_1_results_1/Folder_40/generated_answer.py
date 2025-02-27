def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, num + 1):
        if num * i > 0:
            multiples.append(num * i)
    return sum(multiples[:2])