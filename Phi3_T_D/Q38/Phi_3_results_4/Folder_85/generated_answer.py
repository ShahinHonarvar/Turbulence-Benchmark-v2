def find_subset_of_length_n(elements):
    total_combinations = 1
    subset_length = 23
    for i in range(len(elements), subset_length):
        total_combinations *= i
    for i in range(len(elements) - subset_length + 1, len(elements) + 1):
        total_combinations //= i
    return total_combinations