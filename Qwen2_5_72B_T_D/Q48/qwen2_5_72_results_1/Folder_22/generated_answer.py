def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    present_numbers = set(numbers[41:200])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    example_tuple = tuple(range(101)) + (102, 104, 106, 108, 110, 150, 152) + tuple(range(155, 251))
    print(return_binary_or_hexa(example_tuple))
    example_tuple2 = tuple(range(251))
    print(return_binary_or_hexa(example_tuple2))