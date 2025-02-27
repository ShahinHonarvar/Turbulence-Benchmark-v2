def return_binary_or_hexa(tup):
    a = tup[80]
    b = tup[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum += i
    if isodd(sum):
        return format(sum, 'b')
    else:
        return format(sum, 'x')