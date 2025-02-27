def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    present_numbers = set(numbers[21:36])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]