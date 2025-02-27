from math import comb

def find_subset_of_length_n(elements_set):
    count = 0
    for subset_len in range(96):
        if len(elements_set) >= subset_len:
            count += comb(len(elements_set), subset_len)
    return count