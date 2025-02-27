def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    sequence = set(numbers[77:85])
    missing_sum = sum((x for x in range(a + 1, b) if x not in sequence))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].rjust(2, '0').lower()
    else:
        return bin(missing_sum)[2:].rjust(2, '0')