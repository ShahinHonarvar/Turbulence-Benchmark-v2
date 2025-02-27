def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[29], input_tuple[53])
    numbers_in_range = [num for num in range(a + 1, b) if num not in input_tuple[29:54]]
    sum_of_numbers = sum(numbers_in_range)
    if sum_of_numbers % 2 == 1:
        binary_representation = bin(sum_of_numbers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_of_numbers)[2:].upper()
        return hexadecimal_representation