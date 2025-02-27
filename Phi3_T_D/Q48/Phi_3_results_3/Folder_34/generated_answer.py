def return_binary_or_hexa(tupl):
    a = tupl[60]
    b = tupl[200]
    not_present_set = set(range(a + 1, b)) - set(tupl[60:201])
    if not_present_set:
        total_sum = sum(not_present_set)
        return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]
    return ''