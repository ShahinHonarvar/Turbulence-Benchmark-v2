def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[9])
    total_sum = 0
    current_number = a + 1
    index = 1
    while current_number < b:
        if index < 10 and numbers[index] == current_number:
            index += 1
        else:
            total_sum += current_number
        current_number += 1
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]