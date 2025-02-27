def return_binary_or_hexa(t):
    a, *_, b = t
    missing_numbers = set(range(a + 1, b)) - set(t[1:4])
    if missing_numbers:
        total = sum(missing_numbers)
        return bin(total)[2:] if total % 2 else f'{total:#x}'[2:]
    return ''