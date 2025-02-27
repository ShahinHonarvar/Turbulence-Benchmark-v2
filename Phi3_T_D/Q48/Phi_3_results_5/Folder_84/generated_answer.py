def return_binary_or_hexa(t):
    target_range = set(range(t[32] + 1, t[44]))
    for i in range(32, 45):
        if i < 44:
            target_range.discard(t[i])
    total_sum = sum(target_range)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return format(total_sum, 'b')