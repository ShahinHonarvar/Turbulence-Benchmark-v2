def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[2])
    sum_of_integers = sum(range(a + 1, b))
    sum_of_missing_integers = sum((number for number in range(a + 1, b) if number not in numbers))
    if sum_of_missing_integers % 2 == 1:
        binary_representation = bin(sum_of_missing_integers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_of_missing_integers)[2:]
        return hexadecimal_representation.upper()