def return_binary_or_hexa(num_tuple):
    a = num_tuple[10]
    b = num_tuple[100]
    total_sum = sum(range(a + 1, b))
    missing_numbers_sum = sum(set(range(a + 1, b)) - set(num_tuple[10:100]))
    result = '0' if missing_numbers_sum == total_sum else missing_numbers_sum
    return bin(result)[2:].upper() if missing_numbers_sum % 2 else hex(result)[2:]