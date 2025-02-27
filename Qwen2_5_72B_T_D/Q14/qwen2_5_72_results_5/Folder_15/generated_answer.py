def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    first_four = numbers[:4]
    first_four.sort()
    return first_four[1] if len(first_four) > 1 else None