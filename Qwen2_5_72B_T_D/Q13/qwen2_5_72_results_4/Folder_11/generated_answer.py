def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    subsection = numbers[37:52]
    if len(set(subsection)) < 2:
        return None
    largest = max(subsection)
    subsection.remove(largest)
    while subsection and subsection.count(largest) > 0:
        subsection.remove(largest)
    if not subsection:
        return None
    return max(subsection)