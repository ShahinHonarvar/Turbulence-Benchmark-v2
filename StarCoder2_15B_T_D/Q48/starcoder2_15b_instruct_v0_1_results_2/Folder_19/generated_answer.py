def return_binary_or_hexa(numbers):
    a, b = (numbers[1], numbers[4])
    sum_of_missing_integers = sum((i for i in range(a + 1, b) if i not in numbers))
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:].lower()