def find_sum_of_multiples(number):
    total = 0
    for i in range(1, 70):
        total += i * number
    return total