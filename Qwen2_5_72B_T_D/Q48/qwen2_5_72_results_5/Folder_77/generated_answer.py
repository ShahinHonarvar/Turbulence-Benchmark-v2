def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    present_numbers = set(numbers[19:52])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    data = tuple(range(100))
    assert return_binary_or_hexa(data) == ''
    data = tuple(range(100))
    data = data[:18] + data[19:52] + data[52:]
    assert return_binary_or_hexa(data) == '1001011110001111111110000000000000000000000000'
    data = data[:18] + (100, 101, 102) + data[18:]
    assert return_binary_or_hexa(data) == '9b8ff800'
    print('All checks passed.')