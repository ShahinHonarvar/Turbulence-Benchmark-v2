def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    first_three.sort()
    return first_three[1] if len(first_three) == 3 else None