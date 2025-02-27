def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    sum_of_integers = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers -= i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    elif sum_of_integers != 0:
        return hex(sum_of_integers)[2:]
    else:
        return ''