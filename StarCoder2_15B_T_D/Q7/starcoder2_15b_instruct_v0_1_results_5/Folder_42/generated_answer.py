def all_even_ints_inclusive(numbers):
    even_ints = []
    for index, number in enumerate(numbers):
        if index >= 29 and index <= 79 and (number % 2 == 0):
            even_ints.append(number)
    return even_ints