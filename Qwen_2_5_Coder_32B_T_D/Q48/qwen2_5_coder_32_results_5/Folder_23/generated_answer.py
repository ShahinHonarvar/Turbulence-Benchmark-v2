def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[36]
    sum_val = 0
    expected_set = set(range(a + 1, b))
    given_set = set(tup[21:36])
    diff_set = expected_set - given_set
    if diff_set:
        sum_val = sum(diff_set)
        if sum_val % 2:
            return bin(sum_val)[2:]
        else:
            return hex(sum_val)[2:]
    return ''