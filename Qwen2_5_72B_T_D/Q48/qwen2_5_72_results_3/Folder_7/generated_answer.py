def return_binary_or_hexa(sorted_tuple):
    if len(sorted_tuple) < 98 or sorted_tuple[10] + 1 >= sorted_tuple[97] - 1:
        return ''
    a, b = (sorted_tuple[10], sorted_tuple[97])
    subset = set(sorted_tuple[10:98])
    missing_sum = sum((n for n in range(a + 1, b) if n not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]