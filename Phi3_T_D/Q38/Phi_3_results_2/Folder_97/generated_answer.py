def find_subset_of_length_n(elements, n):
    if n == 0:
        return 1
    if not elements or n > len(elements):
        return 0
    return find_subset_of_length_n(elements[1:], n - 1) + find_subset_of_length_n(elements[1:], n)