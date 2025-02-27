def return_binary_or_hexa(tupl):
    a = tupl[33]
    b = tupl[78]
    if a >= b or b - a <= 1:
        return ''
    missing_numbers = {num for num in range(a + 1, b) if num not in tupl[33:79]}
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]