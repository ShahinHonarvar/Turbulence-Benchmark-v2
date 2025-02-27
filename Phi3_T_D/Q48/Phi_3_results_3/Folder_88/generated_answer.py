def return_binary_or_hexa(seq):
    a, b = (seq[3], seq[9])
    missing_sum = sum((i for i in range(a + 1, b) if i not in seq[3:10]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]