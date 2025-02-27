def sum_even_ints_inclusive(numbers):
    start_index = 56
    end_index = 57
    return sum([num for num in numbers[start_index:end_index + 1] if num % 2 == 0])