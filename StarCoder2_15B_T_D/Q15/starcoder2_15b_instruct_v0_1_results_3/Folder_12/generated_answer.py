def sum_odd_ints_inclusive(int_list):
    start_index = 14
    end_index = 64
    sum_of_odd_ints = 0
    for i, num in enumerate(int_list):
        if start_index <= i <= end_index and num % 2 != 0:
            sum_of_odd_ints += num
    return sum_of_odd_ints