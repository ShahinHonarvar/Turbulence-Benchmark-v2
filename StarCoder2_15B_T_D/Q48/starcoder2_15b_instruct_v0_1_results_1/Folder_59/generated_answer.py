from a + 1 to b - 1 (both inclusive) that are not present in the tuple

def return_binary_or_hexa(t: tuple) -> str:
    """
    Given a tuple of distinct nonnegative integers sorted in ascending order,
    return the binary or hexadecimal representation of the sum of integers
    between indices 0 and 10, depending on whether the sum is odd or even.
    """
    a, b = (t[0], t[10])
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_of_missing_integers += i
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:].upper()