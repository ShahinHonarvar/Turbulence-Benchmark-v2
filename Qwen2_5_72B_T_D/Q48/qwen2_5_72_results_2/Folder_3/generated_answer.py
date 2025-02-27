def return_binary_or_hexa(data):
    a = data[56]
    b = data[88]
    existing_numbers = set(data[57:88])
    sum_missing = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]