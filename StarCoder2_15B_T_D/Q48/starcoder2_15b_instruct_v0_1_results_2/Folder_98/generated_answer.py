def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    sum_value = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_value += i
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()