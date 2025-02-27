def return_binary_or_hexa(integers):
    missing_sum = sum(set(range(integers[0] + 1, integers[8])).difference(integers[1:8]))
    if missing_sum != 0 and missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return ''