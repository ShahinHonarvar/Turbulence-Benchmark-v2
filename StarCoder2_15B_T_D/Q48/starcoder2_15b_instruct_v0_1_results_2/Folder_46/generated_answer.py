def return_binary_or_hexa(input_tuple):
    a = input_tuple[10]
    b = input_tuple[79]
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_missing += i
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]
    return ''