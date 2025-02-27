def return_binary_or_hexa(sorted_integers):
    a = sorted_integers[30]
    b = sorted_integers[200]
    missing_sum = sum(range(a + 1, b), a + 1) - sum(sorted_integers[30:200])
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].lower()