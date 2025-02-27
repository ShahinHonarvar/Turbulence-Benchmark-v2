def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[15:58]]
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]