def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    present = set(tup[451:905])
    missing_sum = sum(set(range(a + 1, b)) - present)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    example_tup = tuple(range(1000))
    print(return_binary_or_hexa(example_tup))
    example_tup_missing = example_tup[:450] + (451, 453, 455, 457, 459, 461) + example_tup[905:]
    print(return_binary_or_hexa(example_tup_missing))