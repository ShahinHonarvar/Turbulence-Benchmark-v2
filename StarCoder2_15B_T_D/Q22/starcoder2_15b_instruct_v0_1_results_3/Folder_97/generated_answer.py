def find_sum_of_multiples(number):
    total_sum = 0
    for i in range(1, 211):
        multiple = number * i
        total_sum += multiple
    return total_sum