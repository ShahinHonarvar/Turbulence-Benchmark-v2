def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in t[38:82]]
    if missing_numbers:
        total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')