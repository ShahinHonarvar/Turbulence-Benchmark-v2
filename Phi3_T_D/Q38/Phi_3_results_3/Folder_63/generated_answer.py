def find_subset_of_length_n(input_set):
    LENGTH = 57
    n = len(input_set)
    if n < LENGTH:
        return 0
    return 1 if LENGTH == 1 else n * find_subset_of_length_n(input_set[1:])