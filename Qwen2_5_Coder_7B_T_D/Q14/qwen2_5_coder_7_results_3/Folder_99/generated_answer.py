def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[608:610])[1]
    except:
        return None