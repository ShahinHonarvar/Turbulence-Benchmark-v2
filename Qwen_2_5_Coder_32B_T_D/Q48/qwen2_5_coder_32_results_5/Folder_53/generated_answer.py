def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[200:203]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]