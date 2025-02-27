def return_binary_or_hexa(numbers):
    a, b = (numbers[48], numbers[76])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[49:76]:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum % 2 == 0 and total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''