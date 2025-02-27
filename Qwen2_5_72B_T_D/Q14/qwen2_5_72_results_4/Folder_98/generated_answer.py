def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    seventh_element = numbers[6:7]
    if not seventh_element:
        return None
    return sorted(seventh_element)[0] if seventh_element else None