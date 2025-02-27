def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[a:b + 1]]
    total_sum_missing = sum(missing_numbers)
    if total_sum_missing % 2 == 1:
        return bin(total_sum_missing)[2:]
    else:
        return hex(total_sum_missing)[2:].upper()