def sum_in_range(numbers):
    """Returns the sum of all integers from the given list that are between 368 and 679, both inclusive."""
    return sum((num for num in numbers if 368 <= num <= 679))