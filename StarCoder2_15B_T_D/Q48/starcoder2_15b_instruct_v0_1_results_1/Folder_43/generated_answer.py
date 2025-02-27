def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[10]
    b = tup[28]
    sum_value = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in tup:
            sum_value -= i
    if sum_value % 2 == 0:
        return hex(sum_value)[2:]
    return bin(sum_value)[2:]