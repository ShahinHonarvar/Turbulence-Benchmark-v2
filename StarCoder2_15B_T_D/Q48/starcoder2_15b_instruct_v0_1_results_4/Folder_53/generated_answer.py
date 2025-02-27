from itertools import count

def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    expected_range = set(range(a + 1, b))
    actual_range = set(numbers[201:202])
    missing_numbers = expected_range - actual_range
    if missing_numbers:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2 == 1:
            return bin(sum_of_missing_numbers)[2:]
        else:
            return hex(sum_of_missing_numbers)[2:]
    else:
        return ''