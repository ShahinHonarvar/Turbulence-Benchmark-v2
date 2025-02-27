def return_binary_or_hexa(numbers):
    """
    Returns the binary or hexadecimal representation of the sum of certain integers depending on the sum's value.
    """
    start_index = 110
    end_index = 348
    sum_of_integers = 0
    for i in range(start_index + 1, end_index):
        if i not in numbers:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()