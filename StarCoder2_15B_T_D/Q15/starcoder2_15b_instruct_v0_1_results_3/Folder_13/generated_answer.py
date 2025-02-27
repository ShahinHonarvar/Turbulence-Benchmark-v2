def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in range(len(int_list)):
        if i >= 25 and i <= 87 and (int_list[i] % 2 == 1):
            sum_odd += int_list[i]
    return sum_odd