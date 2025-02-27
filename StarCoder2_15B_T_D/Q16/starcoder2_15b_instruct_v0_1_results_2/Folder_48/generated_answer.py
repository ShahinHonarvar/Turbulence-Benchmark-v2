def sum_even_ints_inclusive(integers):
    filtered_ints = [i for i in integers[533:606] if i % 2 == 0]
    return sum(filtered_ints) if filtered_ints else 0