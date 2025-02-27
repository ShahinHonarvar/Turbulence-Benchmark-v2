def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in numbers[14:70]:
            sum_missing += i
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]