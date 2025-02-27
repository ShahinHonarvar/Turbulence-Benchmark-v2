def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers[450:906]:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].lstrip('0')
    else:
        return bin(sum_of_integers)[2:].lstrip('0')