def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        binary_representation = bin(sum_of_integers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_of_integers)[2:].upper()
        return hexadecimal_representation