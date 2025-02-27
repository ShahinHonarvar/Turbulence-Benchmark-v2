def return_binary_or_hexa(numbers):
    if len(numbers) < 201 or numbers[70] + 1 >= numbers[200] - 1:
        return ''
    a, b = (numbers[70], numbers[200])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[71:200]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]