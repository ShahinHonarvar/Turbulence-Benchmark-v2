def return_binary_or_hexa(numbers):
    if len(numbers) < 71:
        return ''
    a = numbers[43]
    b = numbers[70]
    present_numbers = set(numbers[43:70])
    sum_missing = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]