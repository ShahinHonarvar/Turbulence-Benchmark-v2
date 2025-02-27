def find_largest_num(numbers):
    try:
        return max(numbers[8:10])
    except IndexError:
        return None