def find_sum_of_multiples(argument):
    running_total = 0
    for i in range(1, 25):
        running_total += argument * i
    return running_total