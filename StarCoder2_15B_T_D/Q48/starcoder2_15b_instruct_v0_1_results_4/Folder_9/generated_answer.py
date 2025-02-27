def return_binary_or_hexa(arg_tuple: tuple) -> str:
    a = arg_tuple[70]
    b = arg_tuple[200]
    numbers_in_range = set(range(a + 1, b))
    numbers_in_tuple = set(arg_tuple[71:200])
    sum_of_missing_numbers = sum(numbers_in_range - numbers_in_tuple)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()