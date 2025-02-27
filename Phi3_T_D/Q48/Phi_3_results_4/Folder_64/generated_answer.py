def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[5])
    missing = {n for n in range(a + 1, b) if n not in numbers}
    missing_sum = sum(missing)
    if missing_sum % 2 == 0:
        return f'{missing_sum:#x}'
    else:
        return f'{missing_sum:b}'