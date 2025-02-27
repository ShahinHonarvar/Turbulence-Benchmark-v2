def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[450:906]]
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()