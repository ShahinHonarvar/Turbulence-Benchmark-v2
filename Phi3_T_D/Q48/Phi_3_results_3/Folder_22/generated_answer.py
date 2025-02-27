def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a, b = (numbers[40], numbers[200])
    sum_absent = sum(set(range(a + 1, b)).difference(numbers[40:201]))
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]