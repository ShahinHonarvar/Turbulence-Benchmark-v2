def return_binary_or_hexa(numbers):
    if len(numbers) <= 871 or len(numbers) < 276:
        return ''
    a = numbers[275]
    b = numbers[871]
    sum_missing = 0
    for num in range(a + 1, b):
        if num not in numbers:
            sum_missing += num
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]