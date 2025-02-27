def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    sum_of_integers = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers -= i
    if sum_of_integers % 2 == 1:
        return format(sum_of_integers, 'b')
    else:
        return format(sum_of_integers, 'x')