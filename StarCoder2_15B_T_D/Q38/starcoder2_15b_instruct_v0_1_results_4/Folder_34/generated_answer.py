def find_subset_of_length_n(elements):
    n = 97
    if len(elements) < n:
        return 0
    count = 0
    for i in range(len(elements) - n + 1):
        subset = elements[i:i + n]
        count += 1
    return count