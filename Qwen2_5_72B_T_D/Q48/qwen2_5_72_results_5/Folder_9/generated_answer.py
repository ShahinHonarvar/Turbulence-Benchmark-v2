def return_binary_or_hexa(numbers):
    if not numbers or len(numbers) < 201:
        return ''
    a = numbers[70]
    b = numbers[200]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[71:200]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check():
    test_tuple = tuple(range(300))
    assert return_binary_or_hexa(test_tuple) == ''
    test_tuple = test_tuple[:71] + (145,) + test_tuple[71:200] + (280,) + test_tuple[200:]
    assert return_binary_or_hexa(test_tuple) == '11011001'
    test_tuple = test_tuple[:71] + (150,) + test_tuple[71:200] + (275,) + test_tuple[200:]
    assert return_binary_or_hexa(test_tuple) == 'd0'
    print('All checks pass.')