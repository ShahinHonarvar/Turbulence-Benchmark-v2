def return_binary_or_hexa(numbers):
    a, *_, b = (numbers[1], *numbers[4])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[1:5]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]