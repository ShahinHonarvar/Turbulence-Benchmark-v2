def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[69:98]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[:-1]