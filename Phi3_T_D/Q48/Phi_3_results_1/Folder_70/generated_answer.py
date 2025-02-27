def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    uniques = set(range(a + 1, b)).difference(numbers[43:70 + 1])
    total = sum(uniques)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]