def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[0], num_tuple[6])
    integer_set = set(num_tuple[1:6])
    missing_sum = sum((i for i in range(a + 1, b) if i not in integer_set))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]