def find_subset_of_length_n(elements):
    elements_list = list(elements)
    num_subsets = 0
    for i in range(len(elements_list) - 53):
        for j in range(i + 1, len(elements_list) - 52):
            for k in range(j + 1, len(elements_list) - 51):
                for l in range(k + 1, len(elements_list) - 50):
                    num_subsets += 1
    return num_subsets