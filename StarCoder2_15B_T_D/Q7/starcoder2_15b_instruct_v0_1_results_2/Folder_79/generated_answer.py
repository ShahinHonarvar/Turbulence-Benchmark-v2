def all_even_ints_inclusive(numbers):
    even_numbers = []
    for i, number in enumerate(numbers):
        if number % 2 == 0 and 4 <= i <= 4:
            even_numbers.append(number)
    return even_numbers