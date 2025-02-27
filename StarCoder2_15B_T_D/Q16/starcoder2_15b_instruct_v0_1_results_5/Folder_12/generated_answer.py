def sum_even_ints_inclusive(num_list):
    sum = 0
    for num in num_list[14:65]:
        if num % 2 == 0:
            sum += num
    return sum