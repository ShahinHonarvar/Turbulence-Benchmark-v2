def all_even_ints_inclusive(numbers):
    even_ints = []
    for i in range(len(numbers)):
        if i >= 29 and i <= 79 and (numbers[i] % 2 == 0):
            even_ints.append(numbers[i])
    return even_ints