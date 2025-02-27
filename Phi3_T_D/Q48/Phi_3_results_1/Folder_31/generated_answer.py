def return_binary_or_hexa(tupl):
    a = tupl[33] if len(tupl) > 33 else 0
    b = tupl[78] if len(tupl) > 78 else 0
    missing_sum = sum((i for i in range(a + 1, b) if i not in tupl[33:78]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]