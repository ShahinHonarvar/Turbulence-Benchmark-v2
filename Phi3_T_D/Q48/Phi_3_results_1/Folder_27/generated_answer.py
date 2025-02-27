def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    missing_sum = sum((val for val in range(a + 1, b) if val not in numbers[86:89]))
    if missing_sum % 2 == 0:
        return hex(missing_sum).replace('0x', '').upper()
    else:
        return bin(missing_sum).replace('0b', '')