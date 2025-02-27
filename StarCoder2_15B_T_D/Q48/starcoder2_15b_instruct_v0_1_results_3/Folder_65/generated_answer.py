def return_binary_or_hexa(tup):
    a = tup[51]
    b = tup[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum += i
    if sum % 2 == 0:
        return format(sum, 'x')
    else:
        return format(sum, 'b')