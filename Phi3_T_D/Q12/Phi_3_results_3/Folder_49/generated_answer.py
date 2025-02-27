def find_smallest_num(numbers):
    try:
        return min(numbers[80:81])
    except IndexError:
        return None