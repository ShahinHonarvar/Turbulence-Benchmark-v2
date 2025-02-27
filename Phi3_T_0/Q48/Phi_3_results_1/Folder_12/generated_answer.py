def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[16:88]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]