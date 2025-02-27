def return_binary_or_hexa(tup: tuple) -> str:
    a, b = (tup[1], tup[4])
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[1:5])
    sum_odd = sum(expected_range - actual_range)
    if sum_odd % 2 == 1:
        return f'{sum_odd:b}'
    else:
        return f'{sum_odd:x}'