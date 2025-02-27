def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    sum_value = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_value += i
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()