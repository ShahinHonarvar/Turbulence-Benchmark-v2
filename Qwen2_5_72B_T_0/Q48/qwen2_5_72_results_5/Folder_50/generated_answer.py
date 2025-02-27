def return_binary_or_hexa(numbers):
    if len(numbers) < 77 or numbers[13] + 1 >= numbers[76] - 1:
        return ''
    a = numbers[13]
    b = numbers[76]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[14:76]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]