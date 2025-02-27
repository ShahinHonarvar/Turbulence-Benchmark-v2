def return_binary_or_hexa(numbers):
    result_sum = sum(set(range(numbers[0] + 1, numbers[4])) - set(numbers[1:numbers[4]]))
    if result_sum == 0 or all((n in numbers[1:numbers[4]] for n in range(numbers[0] + 1, numbers[4]))):
        return ''
    return bin(result_sum)[2:] if result_sum % 2 else hex(result_sum)[2:].upper()