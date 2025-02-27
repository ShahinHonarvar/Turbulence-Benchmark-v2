def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[20]
    b = input_tuple[43]
    summ = 0
    for i in range(a + 1, b):
        if i not in input_tuple[20:43]:
            summ += i
    if summ % 2 == 1:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()