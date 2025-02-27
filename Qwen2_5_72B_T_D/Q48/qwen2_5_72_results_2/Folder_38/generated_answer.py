def return_binary_or_hexa(numbers):
    if len(numbers) <= 36 or len(numbers) <= 85:
        return ''
    a = numbers[36]
    b = numbers[85]
    present = set(numbers[37:85])
    total_sum = sum((x for x in range(a + 1, b) if x not in present))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]