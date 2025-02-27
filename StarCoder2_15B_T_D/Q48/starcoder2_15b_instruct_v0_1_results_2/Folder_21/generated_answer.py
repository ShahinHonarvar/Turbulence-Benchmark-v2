def return_binary_or_hexa(tup: tuple) -> str:
    assert isinstance(tup, tuple) and len(tup) > 0 and all((isinstance(x, int) and x >= 0 for x in tup)), 'Invalid input'
    a = tup[15]
    b = tup[57]
    assert a < b, 'Invalid input'
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]