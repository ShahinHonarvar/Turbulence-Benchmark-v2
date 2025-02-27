def find_smallest_num(numbers):
    try:
        return min(numbers[22:51])
    except ValueError:
        return None