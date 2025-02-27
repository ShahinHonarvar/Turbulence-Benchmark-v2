def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    sum_of_integers = sum(range(a + 1, b))
    present_integers = set(numbers[14:70])
    missing_integers = set(range(a + 1, b)) - present_integers
    sum_of_missing_integers = sum(missing_integers)
    if sum_of_missing_integers % 2 == 0:
        return hex(sum_of_missing_integers)[2:].lstrip('0')
    else:
        return bin(sum_of_missing_integers)[2:].lstrip('0')