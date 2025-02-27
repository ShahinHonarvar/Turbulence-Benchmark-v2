def all_even_ints_inclusive(numbers):
    even_numbers = []
    for i, number in enumerate(numbers):
        if i >= 533 and i <= 605 and (number % 2 == 0):
            even_numbers.append(number)
    return even_numbers