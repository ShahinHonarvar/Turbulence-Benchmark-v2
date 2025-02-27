def return_binary_or_hexa(numbers):
    if len(numbers) < 349 or len(numbers) < 111:
        return ''
    a = numbers[110]
    b = numbers[348]
    subset = set(numbers[111:348])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in subset:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]