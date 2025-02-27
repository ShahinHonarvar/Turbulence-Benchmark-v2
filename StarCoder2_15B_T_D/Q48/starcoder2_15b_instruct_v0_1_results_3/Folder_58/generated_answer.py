def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    integers = list(range(a + 1, b))
    filtered_integers = [num for num in integers if num not in numbers[275:871]]
    sum_of_integers = sum(filtered_integers)
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]