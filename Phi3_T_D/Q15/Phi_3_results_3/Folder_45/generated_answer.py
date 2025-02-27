def sum_odd_ints_inclusive(int_list):
    starting_index = 30
    ending_index = min(len(int_list), 200)
    total = 0
    for i in range(starting_index, ending_index + 1):
        if int_list[i] % 2 != 0:
            total += int_list[i]
    return total