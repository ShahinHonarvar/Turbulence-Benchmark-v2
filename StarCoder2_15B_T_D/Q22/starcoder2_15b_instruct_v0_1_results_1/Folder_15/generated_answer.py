def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, num + 1):
        if num * i > 0 and num * i not in multiples:
            multiples.append(num * i)
        if len(multiples) == 3:
            break
    return sum(multiples)