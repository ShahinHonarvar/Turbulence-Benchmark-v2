def find_subset_of_length_n(elements, n):
    if n == 0:
        return [[]]
    elif len(elements) == 0:
        return []
    else:
        subsets = find_subset_of_length_n(elements[1:], n)
        subsets += [subset + [elements[0]] for subset in find_subset_of_length_n(elements[1:], n - 1)]
        return subsets