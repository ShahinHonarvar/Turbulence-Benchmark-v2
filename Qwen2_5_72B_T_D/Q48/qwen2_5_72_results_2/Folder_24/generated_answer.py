def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    present = set(numbers[13:92])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]