def return_binary_or_hexa(input_tuple):
    a = input_tuple[70]
    b = input_tuple[200]
    sum_not_present = sum((i for i in range(a + 1, b) if i not in input_tuple[70:200]))
    if sum_not_present % 2 != 0:
        binary_repr = bin(sum_not_present)[2:]
        return binary_repr
    else:
        hexa_repr = hex(sum_not_present)[2:].upper()
        return hexa_repr