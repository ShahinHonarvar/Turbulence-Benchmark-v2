def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a, b = (numbers[20], numbers[200])
    if a + 1 >= b:
        return ''
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[21:200]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]