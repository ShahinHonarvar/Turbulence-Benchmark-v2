def sum_even_ints_inclusive(integers):
    sum = 0
    for i in range(70, 85):
        if i < len(integers) and integers[i] % 2 == 0:
            sum += integers[i]
    return sum