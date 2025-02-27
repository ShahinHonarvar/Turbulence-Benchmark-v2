def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    existing_numbers = set(t[51:92])
    missing_sum = sum(set(range(a + 1, b)) - existing_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]