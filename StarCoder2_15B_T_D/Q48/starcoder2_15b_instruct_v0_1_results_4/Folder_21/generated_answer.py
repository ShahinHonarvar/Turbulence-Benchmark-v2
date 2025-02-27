def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    missing_numbers = set(range(a + 1, b)) - set(numbers[16:57])
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]