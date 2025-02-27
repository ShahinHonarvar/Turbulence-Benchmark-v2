def find_subset_of_length_n(elements):
    num_elements = len(elements)
    result = 0
    for i in range(1 << num_elements):
        subset = [elements[j] for j in range(len(elements)) if i & 1 << j]
        if len(subset) == 4:
            result += 1
    return result