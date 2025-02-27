def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_of_integers += i
    return bin(sum_of_integers)[2:] if sum_of_integers % 2 == 1 else hex(sum_of_integers)[2:]