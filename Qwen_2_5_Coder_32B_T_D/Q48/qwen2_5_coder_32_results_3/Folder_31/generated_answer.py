def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    total_sum = 0
    current_number = a + 1
    for num in numbers[34:78]:
        while current_number < num:
            total_sum += current_number
            current_number += 1
        current_number = num + 1
    while current_number < b:
        total_sum += current_number
        current_number += 1
    if total_sum == 0:
        return ''
    else:
        return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]