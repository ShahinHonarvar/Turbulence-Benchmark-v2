def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[11:12]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    example1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18)
    example2 = (1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)
    example3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13)
    print(return_binary_or_hexa(example1))
    print(return_binary_or_hexa(example2))
    print(return_binary_or_hexa(example3))