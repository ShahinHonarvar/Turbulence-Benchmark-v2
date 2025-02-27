def sum_even_ints_inclusive(numbers):
    sum_of_even_ints = 0
    for i in range(310, 371):
        if numbers[i] % 2 == 0:
            sum_of_even_ints += numbers[i]
    return sum_of_even_ints