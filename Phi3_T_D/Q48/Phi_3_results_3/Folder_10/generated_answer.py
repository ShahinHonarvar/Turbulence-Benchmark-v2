def return_binary_or_hexa(input_tuple):
    a = input_tuple[36]
    b = input_tuple[54]
    missing_numbers = [i for i in range(a + 1, b) if i not in input_tuple[36:55]]
    total_sum = sum(missing_numbers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]