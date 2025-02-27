def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[90:98]:
            missing_sum += num
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]