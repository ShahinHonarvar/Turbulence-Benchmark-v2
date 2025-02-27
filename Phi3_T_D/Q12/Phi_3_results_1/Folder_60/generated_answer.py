def find_smallest_num(numbers):
    try:
        return min(numbers[56:58])
    except IndexError:
        return 'Index out of range'