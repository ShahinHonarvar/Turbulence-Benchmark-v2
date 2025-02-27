def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[10]
    b = tup[97]
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[11:97])
    missing_elements = expected_range - actual_range
    if not missing_elements:
        return ''
    sum_missing_elements = sum(missing_elements)
    if sum_missing_elements % 2 == 1:
        return bin(sum_missing_elements)[2:]
    else:
        return hex(sum_missing_elements)[2:]