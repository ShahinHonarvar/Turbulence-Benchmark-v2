def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    needed_numbers = set(range(a + 1, b))
    numbers_in_tuple = set(t[45:49])
    missing_numbers = needed_numbers - numbers_in_tuple
    sum_of_missing_numbers = sum(missing_numbers) if missing_numbers else 0
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]