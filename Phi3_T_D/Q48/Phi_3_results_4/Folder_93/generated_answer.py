def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    sums_not_in_tuple = sum((i for i in range(a + 1, b) if i not in numbers[57:85]))
    if sums_not_in_tuple % 2 == 1:
        return bin(sums_not_in_tuple)[2:]
    else:
        return hex(sums_not_in_tuple)[2:]