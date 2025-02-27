def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for i in range(1, 207):
        sum_of_multiples += number * i
    return sum_of_multiples