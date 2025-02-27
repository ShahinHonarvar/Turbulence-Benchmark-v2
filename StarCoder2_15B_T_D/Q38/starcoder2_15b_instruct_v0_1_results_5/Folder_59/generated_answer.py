def find_subset_of_length_n(set_of_elements):
    count = 0
    for element1 in set_of_elements:
        for element2 in set_of_elements:
            count += 1
    return count