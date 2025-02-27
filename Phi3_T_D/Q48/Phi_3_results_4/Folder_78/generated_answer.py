def return_binary_or_hexa(tup):
    missing_sum = sum(set(range(tup[62] + 1, tup[96])) - set(tup[62:96]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]