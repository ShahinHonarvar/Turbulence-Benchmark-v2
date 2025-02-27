def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    first_smallest = min(first_three)
    first_three.remove(first_smallest)
    return min(first_three) if first_three else None