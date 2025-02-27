def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    for i in range(a + 1, b):
        if i not in numbers:
            sum_value += i
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]