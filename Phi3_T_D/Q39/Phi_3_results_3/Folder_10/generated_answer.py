def return_n_greatest_chars(distinct_string):
    sorted_string = sorted(distinct_string, reverse=True)
    greatest_88_chars = sorted_string[:88]
    return greatest_88_chars