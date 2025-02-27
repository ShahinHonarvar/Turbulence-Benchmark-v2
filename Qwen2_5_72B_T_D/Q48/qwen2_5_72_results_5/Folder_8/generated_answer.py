def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    present_numbers = set(numbers[46:48])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    lst = tuple(range(100))
    print(return_binary_or_hexa(lst))
    lst = lst[:46] + (92, 93, 94) + lst[48:]
    print(return_binary_or_hexa(lst))
    lst = lst[:46] + (47, 93, 94) + lst[48:]
    print(return_binary_or_hexa(lst))