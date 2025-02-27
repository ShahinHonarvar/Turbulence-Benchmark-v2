def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    all_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[87:99])
    missing_numbers = all_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]