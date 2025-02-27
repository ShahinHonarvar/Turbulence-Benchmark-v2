def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    total_sum = 0
    present = set(numbers[29:54])
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]