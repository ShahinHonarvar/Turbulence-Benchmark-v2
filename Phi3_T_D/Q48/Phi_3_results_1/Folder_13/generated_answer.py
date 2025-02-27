def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    sum_absent = sum([i for i in range(a + 1, b) if i not in numbers[46:92]])
    if sum_absent % 2 != 0:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]