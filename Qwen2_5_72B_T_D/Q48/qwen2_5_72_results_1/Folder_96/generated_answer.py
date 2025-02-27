def return_binary_or_hexa(data):
    a = data[50]
    b = data[200]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data[51:200]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()

def check_solution():
    test_data = tuple(range(300))
    result = return_binary_or_hexa(test_data)
    print('Result:', result)
    test_data = (0,) * 50 + (100,) + (0,) * 149 + (200,) + (0,) * 50
    result = return_binary_or_hexa(test_data)
    print('Result:', result)