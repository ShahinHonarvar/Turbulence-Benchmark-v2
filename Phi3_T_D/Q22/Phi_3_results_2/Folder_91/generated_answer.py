def find_sum_of_multiples(integer):
    if integer <= 0:
        return 0
    else:
        return sum((integer * i for i in range(1, 7)))