def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    sum_absent = sum(set(range(a + 1, b)).difference(numbers[60:201]))
    return bin(sum_absent)[2:] if sum_absent % 2 else hex(sum_absent)[2:]