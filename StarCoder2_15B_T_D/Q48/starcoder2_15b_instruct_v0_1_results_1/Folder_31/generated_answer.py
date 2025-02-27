def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in numbers[34:78]))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()