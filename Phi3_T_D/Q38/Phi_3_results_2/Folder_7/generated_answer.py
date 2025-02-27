def find_subset_of_length_n(elements_set):
    n = 180
    num_elements = len(elements_set)
    return 1 if n == 0 else 0 if num_elements < n else math.comb(num_elements, n)