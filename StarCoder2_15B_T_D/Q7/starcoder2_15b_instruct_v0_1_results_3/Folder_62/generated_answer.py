def all_even_ints_inclusive(numbers):
    even_numbers = []
    for index, number in enumerate(numbers):
        if index >= 91 and index <= 99 and (number % 2 == 0):
            even_numbers.append(number)
    return even_numbers