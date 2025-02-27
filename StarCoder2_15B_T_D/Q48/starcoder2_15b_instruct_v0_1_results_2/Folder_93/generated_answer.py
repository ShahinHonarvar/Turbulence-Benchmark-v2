def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        binary_representation = format(sum_of_integers, 'b')
        return binary_representation
    else:
        hexadecimal_representation = format(sum_of_integers, 'x')
        return hexadecimal_representation