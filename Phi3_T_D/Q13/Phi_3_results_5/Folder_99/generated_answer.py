def find_second_largest_num(numbers):
    if len(numbers) < 61:
        return None
    dist_numbers = numbers[309:371]
    if len(dist_numbers) < 2:
        return None
    max_num = max(dist_numbers)
    dist_numbers.remove(max_num)
    second_max_num = max(dist_numbers)
    return second_max_num