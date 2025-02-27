def return_binary_or_hexa(tup):
    for i in range(a + 1, b):
        if i not in tup:
            sum += i
    if sum % 2 == 1:
        return format(sum, 'b')
    else:
        return format(sum, 'x')