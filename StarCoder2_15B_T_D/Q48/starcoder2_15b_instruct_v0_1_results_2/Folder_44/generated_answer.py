def return_binary_or_hexa(numbers: tuple) -> str:
    a = numbers[36]
    b = numbers[52]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    else:
        return bin(sum_of_integers)[2:]