def return_binary_or_hexa(lst):
    a = lst[70]
    b = lst[98]
    total = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in lst[70:99]]
    if missing_numbers:
        total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]