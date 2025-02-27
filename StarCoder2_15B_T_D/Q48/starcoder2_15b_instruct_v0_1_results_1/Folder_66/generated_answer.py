def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]