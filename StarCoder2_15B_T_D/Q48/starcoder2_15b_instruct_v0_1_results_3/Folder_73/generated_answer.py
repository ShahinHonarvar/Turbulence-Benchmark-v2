def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    numbers = set(range(a + 1, b))
    present_numbers = set(t[11:76])
    missing_numbers = numbers - present_numbers
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()