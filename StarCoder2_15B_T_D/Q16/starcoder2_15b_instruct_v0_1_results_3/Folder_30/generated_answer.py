def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for number in numbers[55:100]:
        if number % 2 == 0:
            sum_even += number
    return sum_even