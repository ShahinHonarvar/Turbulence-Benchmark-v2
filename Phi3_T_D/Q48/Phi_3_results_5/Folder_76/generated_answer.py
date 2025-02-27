def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    subset = set(t[451:906])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[:-1]