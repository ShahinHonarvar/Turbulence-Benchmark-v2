def find_subset_of_length_n(elements):
    subsets = []
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subset = {elements[i], elements[j]}
            subsets.append(subset)
    return len(subsets)