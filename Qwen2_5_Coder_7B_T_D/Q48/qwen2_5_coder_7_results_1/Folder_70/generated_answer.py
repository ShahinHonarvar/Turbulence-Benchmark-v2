def return_binary_or_hexa(numbers):
    a, b = (numbers[43], numbers[70])
    if a + 1 >= b - 1:
        return ''
    total_sum = sum(range(a + 1, b))
    remaining_numbers = set(range(a + 1, b)) - set(numbers[43:71])
    for num in remaining_numbers:
        total_sum -= num
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]