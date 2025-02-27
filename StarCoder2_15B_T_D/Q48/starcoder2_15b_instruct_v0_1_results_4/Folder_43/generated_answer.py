def return_binary_or_hexa(t):
    integers_in_range = []
    a = t[10]
    b = t[28]
    for i in range(a + 1, b):
        if i not in t:
            integers_in_range.append(i)
    sum_of_integers = sum(integers_in_range)
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()