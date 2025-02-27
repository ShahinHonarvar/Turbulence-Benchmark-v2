def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[200])
    sum_missing = sum((n for n in range(a + 1, b) if n not in numbers[20:200]))
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    return bin(sum_missing)[2:]