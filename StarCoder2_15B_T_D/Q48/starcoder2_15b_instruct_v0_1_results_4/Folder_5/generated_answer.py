def return_binary_or_hexa(input_tuple: tuple) -> str:
    """
    Returns the binary or hexadecimal representation of the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 2 and 8.
    If the sum is an odd number, the function should return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    The binary representation should not be prefixed with '0b'.
    The hexadecimal representation should not be prefixed with '0x'.
    The binary and hexadecimal representations should start with the most significant digit and have no leading zeros.
    The letters in hexadecimal representation can be either in lowercase or uppercase.
    If all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple, the function should return an empty string.
    """
    a = input_tuple[2]
    b = input_tuple[8]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()