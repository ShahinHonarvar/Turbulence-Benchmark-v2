def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[86:100]]
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].lstrip('0')
    return bin(sum_of_missing_numbers)[2:].lstrip('0')