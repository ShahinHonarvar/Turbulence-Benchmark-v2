def find_subset_of_length_n(s):
    n = 49
    num_subsets = 1
    for _ in range(n):
        num_subsets *= len(s)
        s = {el for el in s if el % 2 == 1}
    return num_subsets