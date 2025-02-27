def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in t[18:61]]
    if missing_numbers:
        total_sum += sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')