def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers[2:8]:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    return bin(sum_of_integers)[2:]