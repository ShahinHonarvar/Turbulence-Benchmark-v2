def return_binary_or_hexa(t):
    missing_sum = sum(range(t[70] + 1, t[200])) - sum(t[70:200 + 1])
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]