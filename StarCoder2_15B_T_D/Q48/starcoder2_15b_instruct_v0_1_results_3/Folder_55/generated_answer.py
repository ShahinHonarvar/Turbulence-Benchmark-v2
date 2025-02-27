def return_binary_or_hexa(numbers: tuple) -> str:
    a = numbers[10]
    b = numbers[12]
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()