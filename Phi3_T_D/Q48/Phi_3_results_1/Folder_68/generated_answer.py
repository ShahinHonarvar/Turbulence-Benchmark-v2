def return_binary_or_hexa(numbers):
    if not (isinstance(numbers, tuple) and len(numbers) == 10 and all((isinstance(i, int) and i >= 0 for i in numbers)) and (sorted(numbers) == numbers)):
        return ''
    missing_sum = sum(set(range(numbers[0] + 1, numbers[9])).difference(numbers))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')