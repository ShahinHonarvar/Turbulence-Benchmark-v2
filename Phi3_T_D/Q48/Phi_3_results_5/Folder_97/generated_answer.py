def return_binary_or_hexa(numbers):
    if len(numbers) < 69 or 34 > len(numbers):
        return ''
    a, b = (numbers[34], numbers[69])
    sum_missing = sum(set(range(int(a) + 1, b)).difference(numbers[34:69]))
    if sum_missing:
        return bin(sum_missing)[2:] if sum_missing % 2 != 0 else hex(sum_missing)[2:]
    return ''