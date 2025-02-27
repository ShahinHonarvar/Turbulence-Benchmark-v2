def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[50:93]]
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].upper()
    else:
        return bin(sum_of_missing)[2:]