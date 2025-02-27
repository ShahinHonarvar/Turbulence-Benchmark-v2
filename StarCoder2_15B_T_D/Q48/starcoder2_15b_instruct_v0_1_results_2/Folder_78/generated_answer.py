def return_binary_or_hexa(input_tuple):
    a = input_tuple[62]
    b = input_tuple[96]
    missing_integers = set(range(a + 1, b)) - set(input_tuple[63:96])
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 1:
        binary_representation = bin(sum_missing_integers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_missing_integers)[2:].upper()
        return hexadecimal_representation