def find_second_smallest_num(numbers):
    if len(numbers) < 151:
        return None
    starting = min(range(50, 201), key=numbers.__getitem__)
    numbers[starting] = float('inf')
    second_smallest = min(range(50, 201), key=numbers.__getitem__)
    return numbers[second_smallest] if numbers[second_smallest] != float('inf') else None