def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    total = 0
    num_set = set(numbers[11:100])
    for i in range(a + 1, b):
        if i not in num_set:
            total += i
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]