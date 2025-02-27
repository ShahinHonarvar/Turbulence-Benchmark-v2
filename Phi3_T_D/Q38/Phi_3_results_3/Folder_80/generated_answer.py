def find_subset_of_length_n(elements_set):
    n = 36
    count = 1
    for element in elements_set:
        count *= len(elements_set) - n + 1
    return count // math.factorial(n)