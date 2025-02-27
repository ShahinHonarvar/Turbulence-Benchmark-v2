def return_binary_or_hexa(numbers):
    missing_numbers = []
    for i in range(numbers[9] + 1, numbers[27]):
        if i not in numbers:
            missing_numbers.append(i)
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()