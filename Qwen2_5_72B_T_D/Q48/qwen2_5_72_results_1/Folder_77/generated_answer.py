def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    sum_missing = 0
    for num in range(a + 1, b):
        if num not in numbers:
            sum_missing += num
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]