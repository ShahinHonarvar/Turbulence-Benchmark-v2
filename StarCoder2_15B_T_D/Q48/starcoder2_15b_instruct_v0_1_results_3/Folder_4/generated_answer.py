def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    numbers_set = set(numbers)
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers_set:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]