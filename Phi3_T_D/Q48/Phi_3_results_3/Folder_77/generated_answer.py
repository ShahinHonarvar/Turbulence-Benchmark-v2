def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    absent_sum = sum((i for i in range(a + 1, b) if i not in numbers[18:53]))
    if absent_sum == 0:
        return ''
    if absent_sum % 2 != 0:
        return bin(absent_sum)[2:]
    else:
        return hex(absent_sum)[2:]