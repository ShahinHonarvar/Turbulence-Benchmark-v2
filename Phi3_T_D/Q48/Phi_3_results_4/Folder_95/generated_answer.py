def return_binary_or_hexa(sorted_non_neg_ints):
    a, b = (sorted_non_neg_ints[32], sorted_non_neg_ints[99])
    missing_sum = sum(set(range(a + 1, b)) - set(sorted_non_neg_ints[32:99]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]