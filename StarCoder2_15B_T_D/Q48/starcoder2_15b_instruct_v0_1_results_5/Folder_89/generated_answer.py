def return_binary_or_hexa(tup: tuple) -> str:
    """
    Returns the binary or hexadecimal representation of the sum of integers from a + 1 to b - 1 (both inclusive)
    that are not present in the tuple between indices 55 and 84.
    """
    a = tup[55]
    b = tup[84]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    else:
        return bin(sum_of_integers)[2:]