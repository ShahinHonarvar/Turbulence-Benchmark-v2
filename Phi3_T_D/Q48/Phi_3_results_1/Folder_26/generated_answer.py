def return_binary_or_hexa(integers):
    a = integers[68]
    b = integers[99]
    missing_sum = sum((i for i in range(a + 1, b) if i not in integers[68:99 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]