def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for number in int_list[209:557]:
        if number % 2 == 0:
            even_sum += number
    return even_sum