def return_binary_or_hexa(my_tuple: tuple) -> str:
    a = my_tuple[13]
    b = my_tuple[76]
    numbers_in_range = set(range(a + 1, b))
    numbers_not_in_tuple = numbers_in_range - set(my_tuple)
    sum_of_numbers = sum(numbers_not_in_tuple)
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]