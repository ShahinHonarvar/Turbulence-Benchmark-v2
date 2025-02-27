def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[91:97]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example_tuple = tuple(range(100))
    example_tuple = example_tuple[:90] + (89, 91, 92, 93, 94, 95, 96, 98)
    print(return_binary_or_hexa(example_tuple))