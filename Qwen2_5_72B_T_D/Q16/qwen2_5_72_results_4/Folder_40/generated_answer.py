def sum_even_ints_inclusive(numbers):
    even_sum = 0
    for number in numbers[:3]:
        if number % 2 == 0:
            even_sum += number
    return even_sum