def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[16]
    b = numbers_tuple[87]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers_tuple[16:88]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]