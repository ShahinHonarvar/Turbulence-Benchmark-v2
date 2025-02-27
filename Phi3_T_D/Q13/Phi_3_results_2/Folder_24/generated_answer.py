def find_second_largest_num(numbers):
    try:
        return sorted(numbers[74:95])[-2] if len(set(numbers[74:95])) >= 2 else None
    except IndexError:
        return None