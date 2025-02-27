def all_ints_inclusive(numbers):
    if len(numbers) > 51:
        return numbers[43:52]
    return numbers[min(43, len(numbers)):]