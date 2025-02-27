def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    subset = numbers[40:81]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1]