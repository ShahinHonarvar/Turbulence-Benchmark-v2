def return_binary_or_hexa(numbers):
    if len(numbers) < 81 or len(numbers) < 26:
        return ''
    a = numbers[25]
    b = numbers[80]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_tuple = tuple((i for i in range(101) if i != 30 and i != 31))
    assert return_binary_or_hexa(test_tuple) == '31', f"Test 1 failed, expected '31', got {return_binary_or_hexa(test_tuple)}"
    test_tuple2 = tuple((i for i in range(101)))
    assert return_binary_or_hexa(test_tuple2) == '', f"Test 2 failed, expected '', got {return_binary_or_hexa(test_tuple2)}"
    test_tuple3 = (i for i in range(0, 101, 2))
    assert return_binary_or_hexa(test_tuple3) == '1406', f"Test 3 failed, expected '1406', got {return_binary_or_hexa(test_tuple3)}"
    test_tuple4 = tuple((i for i in range(25, 105) if i < 55 or i > 80))
    assert return_binary_or_hexa(test_tuple4) == '7ff', f"Test 4 failed, expected '7ff', got {return_binary_or_hexa(test_tuple4)}"