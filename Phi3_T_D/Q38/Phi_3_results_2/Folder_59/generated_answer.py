def find_subset_of_length_n(elements_set):
    count_subsets = 0
    for item in elements_set:
        for next_item in elements_set - {item}:
            if next_item > item:
                count_subsets += 1
    return count_subsets