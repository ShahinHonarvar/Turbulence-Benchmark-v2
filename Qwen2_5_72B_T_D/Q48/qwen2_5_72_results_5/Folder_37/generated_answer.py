def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    present_numbers = set(numbers[3:7])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]