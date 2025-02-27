def return_binary_or_hexa(tup):
    a = tup[11]
    b = tup[76]
    sum_of_nums = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_nums += i
    if sum_of_nums % 2 == 1:
        return bin(sum_of_nums)[2:]
    else:
        return hex(sum_of_nums)[2:].upper()