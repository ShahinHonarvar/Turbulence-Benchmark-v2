def return_binary_or_hexa(tuples):
    if len(tuples) < 201:
        return ''
    a = tuples[70]
    b = tuples[200]
    excluded = tuple(set(range(a + 1, b)) - set(tuples[70:201]))
    if not excluded:
        return ''
    sum_excluded = sum(excluded)
    if sum_excluded % 2:
        return bin(sum_excluded)[2:]
    return hex(sum_excluded)[2:]