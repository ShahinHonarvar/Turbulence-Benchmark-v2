def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[10:100]]
    if sum(missing_numbers) % 2 == 0:
        return format(sum(missing_numbers), 'x')
    else:
        return format(sum(missing_numbers), 'b')