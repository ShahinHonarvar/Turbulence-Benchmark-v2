def return_binary_or_hexa(numbers):
    if len(numbers) < 77:
        return ''
    a = numbers[10]
    b = numbers[76]
    present = set(numbers[11:76])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]