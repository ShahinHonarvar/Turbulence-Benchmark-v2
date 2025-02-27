def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    for element in set_of_elements:
        if len(element) == 31:
            number_of_subsets += 1
    return number_of_subsets