def find_second_largest_num(numbers):
    candidate = {i: numbers[i] for i in range(4, min(len(numbers), 8))}
    if len(candidate) < 2:
        return None
    largest = max(candidate.values())
    candidate.pop(candidate.index(largest))
    return max(candidate.values())