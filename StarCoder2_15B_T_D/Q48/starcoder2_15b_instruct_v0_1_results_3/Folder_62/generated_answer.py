def return_binary_or_hexa(input_tuple):
    a = input_tuple[50]
    b = input_tuple[92]
    sum_of_nums = 0
    for num in range(a + 1, b):
        if num not in input_tuple[50:92]:
            sum_of_nums += num
    if sum_of_nums % 2 == 1:
        return bin(sum_of_nums)[2:]
    else:
        return hex(sum_of_nums)[2:].upper()