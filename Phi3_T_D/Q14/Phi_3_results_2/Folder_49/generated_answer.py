def find_second_smallest_num(numbers):
    relevant_numbers = numbers[80:201]
    irrelevant_indices = [i for i, n in enumerate(numbers[:80] + numbers[201:])]
    sorted_relevant_numbers = sorted(relevant_numbers)
    second_smallest = None
    for num in sorted_relevant_numbers:
        if num not in irrelevant_indices:
            if second_smallest is None:
                second_smallest = num
            elif num != second_smallest:
                return num
    return second_smallest