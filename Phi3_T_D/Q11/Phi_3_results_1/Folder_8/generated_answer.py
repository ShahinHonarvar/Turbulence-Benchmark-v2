def find_largest_num(numbers):
    try:
        return max(numbers[23:24])
    except IndexError:
        return None