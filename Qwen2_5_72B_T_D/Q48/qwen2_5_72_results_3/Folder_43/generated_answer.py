def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    present = set(numbers[11:28])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]

def check_function():
    test_tuple = tuple(range(0, 100, 2))
    print(return_binary_or_hexa(test_tuple))