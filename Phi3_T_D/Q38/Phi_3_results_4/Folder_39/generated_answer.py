def find_subset_of_length_n(elements):
    n = 59
    if n < 0 or n > len(elements):
        return 0
    sum_ = 0
    for i in range(2 ** len(elements)):
        count = bin(i).count('1') - 1
        if count == n:
            sum_ += 1
    return sum_