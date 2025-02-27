def find_second_smallest_num(numbers):
    if 608 < len(numbers) and len(numbers) > 609:
        numbers[608:609] = sorted(numbers[608:609])
        return numbers[608]
    return None