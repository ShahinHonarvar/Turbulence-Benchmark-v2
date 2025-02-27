def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    sum_value = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers]
    if sum_value == sum(missing_numbers):
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()