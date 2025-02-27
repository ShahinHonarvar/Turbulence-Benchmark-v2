def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in t:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()