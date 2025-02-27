def return_binary_or_hexa(my_tuple):
    a = my_tuple[3]
    b = my_tuple[9]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in my_tuple[3:10]:
            sum_of_numbers += i
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()