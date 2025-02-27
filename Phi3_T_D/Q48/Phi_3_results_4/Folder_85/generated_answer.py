def return_binary_or_hexa(data):
    a, _, _, _, _, _, _, _, b = data
    missing = sum(set(range(a + 1, b)).difference(data[1:8]))
    if missing % 2 != 0:
        return bin(missing)[2:]
    else:
        return hex(missing)[2:]