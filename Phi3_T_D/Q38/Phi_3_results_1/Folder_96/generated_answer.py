def find_subset_of_length_n(s):
    if len(s) < 47:
        return 0
    return 1 + find_subset_of_length_n(s[1:]) + find_subset_of_length_n(s[1:])