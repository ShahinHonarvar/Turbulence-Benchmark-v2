def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    present_numbers = set(numbers[201:202])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]