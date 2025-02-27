def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[43:87]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_case = tuple((i for i in range(100) if i != 50 and i != 55))
    result = return_binary_or_hexa(test_case)
    print(f'Test Result: {result}')