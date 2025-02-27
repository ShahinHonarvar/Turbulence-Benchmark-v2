def return_binary_or_hexa(numbers):
    a, b = (numbers[200], numbers[202])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[200:203]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]