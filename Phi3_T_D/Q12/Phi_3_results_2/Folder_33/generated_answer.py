def find_smallest_num(numbers):
    try:
        return min(numbers[527:539])
    except ValueError:
        return None