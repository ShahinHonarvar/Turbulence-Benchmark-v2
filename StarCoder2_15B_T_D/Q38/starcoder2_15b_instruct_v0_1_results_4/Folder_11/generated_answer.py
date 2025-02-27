def find_subset_of_length_n(elements):
    """Find the number of all subsets of size 77 in a given set of elements."""
    subsets = []
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for n in range(m + 1, len(elements)):
                            for o in range(n + 1, len(elements)):
                                subset = {elements[i], elements[j], elements[k], elements[l], elements[m], elements[n], elements[o]}
                                subsets.append(subset)
    return len(subsets)