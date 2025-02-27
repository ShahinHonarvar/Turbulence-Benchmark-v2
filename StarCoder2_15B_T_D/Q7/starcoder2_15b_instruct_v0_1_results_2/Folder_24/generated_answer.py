def all_even_ints_inclusive(numbers):
    even_ints = []
    for i in range(74, 96):
        if numbers[i] % 2 == 0:
            even_ints.append(numbers[i])
    return even_ints