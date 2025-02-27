def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    missing_sum = sum(range(a + 1, b)) - sum(t[2:6])
    return bin(missing_sum)[2:] if missing_sum % 2 else '{:x}'.format(missing_sum)