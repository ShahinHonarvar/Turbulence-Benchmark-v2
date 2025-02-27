def find_subset_of_length_n(s):
    n = 66
    count = 1
    for element in s:
        count *= len(s) - element
    return count // (n * (len(s) - n) ** (n - 1))