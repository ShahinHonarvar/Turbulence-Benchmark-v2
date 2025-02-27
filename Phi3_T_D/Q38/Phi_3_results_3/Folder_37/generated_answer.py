def find_subset_of_length_n(elements_set):
    result = 0
    n = 28
    total = 2 ** len(elements_set)
    if n > len(elements_set):
        return 0
    for i in range(total):
        bin_str = bin(i)[2:].zfill(len(elements_set))
        bin_list = [int(c) for c in bin_str]
        if bin_list.count(1) == n:
            result += 1
    return result