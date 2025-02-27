def return_binary_or_hexa(t):
    missing_sum = sum(set(range(t[69] + 1, t[97])) - set(t[69:97]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]