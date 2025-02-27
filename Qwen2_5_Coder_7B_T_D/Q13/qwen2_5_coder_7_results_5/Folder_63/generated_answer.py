def find_second_largest_num(numbers):
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    largest = max(subset[0], subset[1])
    second_largest = min(subset[0], subset[1])
    for number in subset[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest if second_largest != largest else None