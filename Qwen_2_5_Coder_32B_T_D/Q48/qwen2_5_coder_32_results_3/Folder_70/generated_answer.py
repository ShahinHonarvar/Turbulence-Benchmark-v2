def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    present = set(numbers[44:70])
    total_sum = 0
    for number in range(a + 1, b):
        if number not in present:
            total_sum += number
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]