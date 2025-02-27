def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    present = set(numbers[51:92])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]