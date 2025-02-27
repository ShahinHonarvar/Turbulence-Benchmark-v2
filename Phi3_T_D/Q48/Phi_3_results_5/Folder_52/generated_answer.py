def return_binary_or_hexa(numbers):
    start_index = 38
    end_index = 81
    a = numbers[start_index]
    b = numbers[end_index]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[start_index:end_index + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]