def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    number_set = set(numbers)
    missing_integers = []
    for i in range(a + 1, b):
        if i not in number_set:
            missing_integers.append(i)
    sum_of_missing_integers = sum(missing_integers)
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]